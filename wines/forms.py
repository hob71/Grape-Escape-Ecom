from .models import Product, Region, Cheese
from django import forms


class wineform(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('wine_type',
                  'wine_region',
                  'recommended_cheese',
                  'name',
                  'description',
                  'price',
                  'image',
                  'offer',)


class regionform(forms.ModelForm):

    class Meta:
        model = Region
        fields = ('name',
                  'description',)


class cheeseform(forms.ModelForm):

    class Meta:
        model = Cheese
        fields = ('name',
                  'description',)
