from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        labels = {
            'category': 'Барааны Ангилал',
            'product_name': 'Барааны Нэр',
            'stock': 'Үнэ',
        }

