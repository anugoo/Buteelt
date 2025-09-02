from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['pcategory', 'pname', 'price']
        labels = {
            'pcategory': 'Барааны Ангилал',
            'pname': 'Барааны Нэр',
            'price': 'Үнэ',
        }

