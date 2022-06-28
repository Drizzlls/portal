from django import forms
from .models import *

class AddItem(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['title','description','price','brand','category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control','rows':3}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'inventoryNumber': forms.NumberInput(attrs={'class': 'form-control'}),
            'brand': forms.Select(attrs={'class': 'form-select'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
        }
