from django.shortcuts import render, redirect
from .models import Wishlist, WishlistItem
from products.models import Product
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def wishlist(request):
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)

    wishlist_items = WishlistItem.objects.filter(wishlist=wishlist)

    return render(request, 'wishlist/wishlist_items.html', {'wishlist_items': wishlist_items})

@login_required
def add_to_wishlist(request, id):
    product = Product.objects.get(id=id)
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    wishlist_item, created = WishlistItem.objects.get_or_create(wishlist=wishlist, product=product)

    return redirect('wishlist-items')

@login_required
def remove_wishlist_item(request, id):
    wishlist = Wishlist(user=request.user)
    wishlist_item = WishlistItem.objects.get(id=id)

    if wishlist_item:
        wishlist_item.delete()
        messages.success(request, "Item removed from wishlist")
    
    return redirect('wishlist-items')