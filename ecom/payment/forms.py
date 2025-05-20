from django import forms
from django.db import models
from .models import ShippingAddress

class ShippingForm(forms.ModelForm):
    shipping_fullname = forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'full name'}),required=True)
    shipping_email= forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'email'}),required=True)
    shipping_address1= forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'address1'}),required=True)
    shipping_address2= forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'address2'}),required=False)
    shipping_city= forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'city'}),required=True)
    shipping_state= forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'state'}),required=True)
    shipping_pincode= forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'pincode'}),required=True)
    shipping_country= forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'country'}),required=True)

    class Meta:
        model=ShippingAddress
        fields=['shipping_fullname','shipping_email','shipping_address1','shipping_address2','shipping_city','shipping_state','shipping_pincode','shipping_country']

        exclude=['user',]

