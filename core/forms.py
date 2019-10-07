from django.forms import ModelForm
from django import forms
from . models import Purchase

class PurchaseForm(ModelForm):
    class Meta:
        model = Purchase
        fields = ['name', 'phone', 'address', 'medicine', 'purchase_date', 'clearance_status']

