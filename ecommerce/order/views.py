from django.shortcuts import render, redirect
from account.models import Address
from products.models import Product
from cart.models import Cart, CartItem
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Order, OrderItem

# Create your views here.
@login_required
def checkout(request):
    cart = Cart.objects.get(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    addresses = Address.objects.filter(user=request.user)

    if not cart_items:
        messages.error(request, "Your cart has no items. Can't place order")
        return redirect("products-list")

    return render(request, 'order/checkout.html', {'cart_items':cart_items, 'addresses': addresses, 'cart': cart})


@login_required
def place_order(request):
    cart = Cart.objects.get(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    
    if request.method == 'POST':
        address_id = request.POST.get('address')
        selected_address = Address.objects.get(id=address_id)

        order = Order.objects.create(user=request.user, address=selected_address, total_amount=cart.total_amount)

        for item in cart_items:
            order_item = OrderItem.objects.create(order=order, product=item.product, quantity=item.quantity, price=item.total_price)
            # now we will also need to reduce the particular products quantity / stock as it has been bought by some user
            product = order_item.product
            product.stock -= order_item.quantity
            print(product.stock)
            product.save()

        cart_items.delete()
        messages.success(request, 'Order placed successfully! Continue Shopping')
        
        request.session['order_success'] = True
        return redirect('order-success')
    else:
        messages.error(request, 'Something went wrong! Order not placed yet. Try again!')
    return redirect('order-checkout')

@login_required
def orders(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')

    return render(request, 'order/orders.html', {'orders': orders})

@login_required
def order_detail(request, id):
    order = Order.objects.get(user=request.user, id=id)
    order_items = order.orderitem_set.all()

    return render(request, 'order/order-details.html', {"order_items": order_items, 'order': order})


def order_success(request):

    if not request.session.get('order_success'):
        return redirect('products-list')

    del request.session['order_success']
    return render( request, 'order/order_success.html')