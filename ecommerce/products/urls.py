from django.urls import path
from .import views

urlpatterns = [
    path('', views.AllProducts.as_view(), name='products-list'),
    path('product-detail/<int:pk>', views.ProductDetail.as_view(), name='products-detail'),
    path('category/', views.categoryFilter, name='products-filter'),
]