import uuid

from django.db import models
from django.db.models import Sum
from wines.models import Product
from profiles.models import UserProfile
from decimal import *


class order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False, unique=True)
#    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders')  # added from Code institute tutorial
    firstname = models.CharField(max_length=20, null=False, blank=False)
    lastname = models.CharField(max_length=30, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = models.CharField(max_length=30, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=100, null=False, blank=False)
    street_address2 = models.CharField(max_length=100, null=True, blank=True)
    county = models.CharField(max_length=60, null=True, blank=True)
    delivery_cost = models.DecimalField(max_digits=20, decimal_places=2, null=False, default=0.00)
    order_total = models.DecimalField(max_digits=20, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=20, decimal_places=2, null=False, default=0)

    def _generate_order_number(self):
        return uuid.uuid4().hex.upper()

    def update_total(self):
        delivery_cost = Decimal(5.00)
        self.order_total = self.ordered_item.aggregate(Sum('ordered_item_total'))['ordered_item_total__sum'] or 0
        self.grand_total = self.order_total + delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


# orderlineitem taken from Code Institue miniproject

class orderlineitem(models.Model):
    order = models.ForeignKey(order, null=False, blank=False, on_delete=models.CASCADE, related_name='ordered_item')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    ordered_item_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        self.ordered_item_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order.order_number
