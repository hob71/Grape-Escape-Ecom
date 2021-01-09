from django.contrib import admin
from .models import orderlineitem, order


class orderitemadministrator(admin.TabularInline):
    model = orderlineitem


class orderadministration(admin.ModelAdmin):
    list_display = ('order_number',
                    'firstname',
                    'lastname',
                    'email',
                    'phone_number',
                    'postcode',
                    'town',
                    'street_address1',
                    'street_address2',
                    'county',
                    'country',
                    'delivery_cost',
                    'order_total',
                    'grand_total',)

    inlines = (orderitemadministrator,)


admin.site.register(order, orderadministration)
