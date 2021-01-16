from django.contrib import admin
from .models import Product, Region, Cheese


class ProdAdmin(admin.ModelAdmin):
    list_display = (
        'wine_type',
        'wine_region',
        'recommended_cheese',
        'name',
        'description',
        'price',
        'image',
        'offer',
    )


class RegionAdmin(admin.ModelAdmin):
        list_display = ('name',
                        'description',)


class CheeseAdmin(admin.ModelAdmin):
        list_display = ('name',
                        'description',)


admin.site.register(Product, ProdAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(Cheese, CheeseAdmin)
