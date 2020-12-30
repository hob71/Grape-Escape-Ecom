from django.db import models


class Product(models.Model):
    class Meta:
        verbose_name_plural = 'Products'
    cat = models.CharField(max_length= 100, null=True)
    name = models.CharField(max_length=150, null=False, blank=False)
    description = models.CharField(max_length=400, null=False, blank=False)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False)
    image = models.ImageField(null=True, blank=True)
    offer = models.BooleanField(null=True)

    def __str__(self):
        return self.name
