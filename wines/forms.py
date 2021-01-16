from .models import Product
from django import forms


class wineform(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('wine_type',
                  'name',
                  'description',
                  'price',
                  'image',
                  'offer',)
