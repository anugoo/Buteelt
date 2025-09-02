from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product  # загварыг импортлоно

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_product')  # амжилттай хадгалахад дахин өөртөө орно
    else:
        form = ProductForm()

    products = Product.objects.all()  # бүх барааг авна

    return render(request, 'create_product.html', {'form': form, 'products': products})
def product_success(request):
    return render(request, 'product_success.html')
