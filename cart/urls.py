from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_items, name='cart-items' ),
    path('update-quantity/<int:id>', views.quantity, name='cart-item_quantity' ),
    path('add-to-cart/<int:id>', views.add_to_cart, name='cart-add' ),
    path('remove-item/<int:id>', views.remove_item, name='cart-remove' ),
]