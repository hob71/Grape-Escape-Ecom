from django import forms
from .models import UserProfile


class profileform(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

# code from Code Institute mini project
    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_town': 'Town',
            'default_street_address1': 'Street Line 1',
            'default_street_address2': 'Street Line 2',
            'default_postcode': 'Postcode',
            'default_county': 'County',
            'default_country': 'Country',
        }

        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False