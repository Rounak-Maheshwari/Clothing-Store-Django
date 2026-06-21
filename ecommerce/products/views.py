from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product
from django.db.models import Q

# Create your views here.

class AllProducts(ListView):
    model = Product
    template_name = 'products/product-list.html'
    context_object_name = 'products'

class ProductDetail(DetailView):
    model = Product
    template_name = 'products/product-detail.html'
    context_object_name = 'product'

def categoryFilter(request):
    query = request.GET.get('q')

    if query:
        products = Product.objects.filter(
            Q(title__icontains = query) |
            Q(description__icontains = query) |
            Q(category__name__icontains = query)
        )

    return render(request, 'products/product-list.html', {'products': products})