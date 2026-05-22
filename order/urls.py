from django.urls import path
from . import views

urlpatterns = [
    path('checkout/', views.checkout, name='order-checkout'),
    path('place-order/', views.place_order, name='order-place'),
    path('all-orders/', views.orders, name='order-all_orders'),
    path('order-details/<int:id>', views.order_detail, name='order-detail'),
    path('order-success/', views.order_success, name='order-success'),
]