from django.contrib import admin
from .models import Product


class ProdAdmin(admin.ModelAdmin):
    list_display = (
        'wine_type',
        'name',
        'description',
        'price',
        'image',
        'offer',
    )


admin.site.register(Product, ProdAdmin)
