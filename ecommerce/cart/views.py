from django.shortcuts import render, get_object_or_404, redirect
from .models import CartItem, Cart
from django.contrib.auth.decorators import login_required
from products.models import Product
from django.contrib import messages

# Create your views here.
@login_required
def cart_items(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)

    return render(request, 'cart/cart.html', {'cart_items': cart_items, 'cart': cart})

@login_required
def add_to_cart(request, id):

    product = get_object_or_404(Product, id=id)

    cart, created = Cart.objects.get_or_create(user=request.user)

    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    if not created:
        cart_item.quantity += 1
        cart_item.save()
        messages.success(request, "Item added to the cart")
    
    return redirect('cart-items')

def quantity(request, id):
    cart = Cart.objects.get(user=request.user)
    if request.method == 'POST':
        cart_item = CartItem.objects.get(cart=cart, id=id)
        quantity = request.POST.get('quantity')

        if int(quantity) > cart_item.product.stock:
            messages.warning(request, f"You can buy at max {cart_item.product.stock} items of {cart_item.product.title}") 
            return redirect('cart-items')

        else:
            cart_item.quantity = quantity
            cart_item.save()
    return redirect('cart-items')


def remove_item(request, id):
    
    cart = Cart.objects.get(user=request.user)

    cart_item = CartItem.objects.get(id=id)

    if cart_item:
        cart_item.delete()
        messages.success(request, 'Item removed successfully from the cart!')
    
    return redirect('cart-items')

