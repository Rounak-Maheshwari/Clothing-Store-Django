from django.db import models
from products.models import Product
from django.contrib.auth.models import User


# Create your models here.


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    
    @property
    def quantities(self):
        total_items = 0
        for item in self.cartitem_set.all():
            total_items += item.quantity
        return total_items
    
    @property
    def total_amount(self):
        total = 0

        for item in self.cartitem_set.all():
            total += item.total_price
        
        return total

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.product.title
    
    @property
    def total_price(self):
        return self.product.price * self.quantity