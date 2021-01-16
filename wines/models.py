from django.db import models
from django.utils.translation import gettext_lazy as _


class Product(models.Model):

    class WineType(models.TextChoices):
        WHITE = 'WHITE', _('White')
        RED = 'RED', _('Red')
        ROSE = 'ROSE', _('Rose')

    class Meta:
        verbose_name_plural = 'Products'

    wine_type = models.CharField(max_length= 100, choices=WineType.choices, default=WineType.WHITE)
    wine_region = models.ForeignKey('Region', on_delete=models.RESTRICT, null=True)
    recommended_cheese = models.ForeignKey('Cheese', on_delete=models.RESTRICT, null=True)
    name = models.CharField(max_length=150, null=False, blank=False)
    description = models.CharField(max_length=400, null=False, blank=False)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False)
    image = models.ImageField(null=True, blank=True)
    offer = models.BooleanField(null=True)

    def __str__(self):
        return self.name


class Region(models.Model):

    class Meta:
        verbose_name_plural = 'Regions'

    name = models.CharField(max_length=150, null=False, blank=False)
    description = models.CharField(max_length=400, null=False, blank=False)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Cheese(models.Model):

    class Meta:
        verbose_name_plural = 'Cheeses'

    name = models.CharField(max_length=150, null=False, blank=False)
    description = models.CharField(max_length=400, null=False, blank=False)

    def __str__(self):
        return self.name
