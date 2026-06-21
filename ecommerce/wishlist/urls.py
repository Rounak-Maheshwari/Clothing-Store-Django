from django.urls import path
from . import views

urlpatterns = [
    path('', views.wishlist, name='wishlist-items'),
    path('add-to-wishlist/<int:id>', views.add_to_wishlist, name='wishlist-add'),
    path('remove-wishlist-item/<int:id>', views.remove_wishlist_item, name='wishlist-remove_item'),
]