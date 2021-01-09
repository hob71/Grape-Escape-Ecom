from django import forms
from .models import order


class orderform(forms.ModelForm):
    class Meta:
        model = order
        fields = ('firstname',
                  'lastname',
                  'email',
                  'phone_number',
                  'postcode',
                  'town',
                  'street_address1',
                  'street_address2',
                  'county',
                  'country',)


# code from Code Institute mini project

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        placeholders = {
            'firstname': 'First Name',
            'lastname': 'Surname',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'postcode': 'Postcode',
            'town': 'Town',
            'street_address1': 'Street Line 1',
            'street_address2': 'Street Line 2',
            'county': 'County',
            'country': 'Country'
        }

        self.fields['firstname'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
