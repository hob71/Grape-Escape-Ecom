from django.contrib import admin
from .models import Product


class ProdAdmin(admin.ModelAdmin):
    list_display = (
        'cat',
        'name',
        'description',
        'price',
        'image',
        'offer',
    )


admin.site.register(Product, ProdAdmin)
