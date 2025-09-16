from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product,Category
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

def signin_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')  # Нэвтэрсний дараа homepage руу шилжүүлнэ
    else:
        form = AuthenticationForm()
    return render(request, 'signin.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')  # Бүртгэл амжилттай бол нэвтрэх хуудас руу шилжүүлнэ
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
def store_view(request):
    # логик
    return render(request, 'store.html')
def cart_view(request):
    # логик
    return render(request, 'cart.html')
def dashboard_view(request):
    # логик
    return render(request, 'dashboard.html')
def order_view(request):
    # логик
    return render(request, 'order_complete.html')
def place_view(request):
    # логик
    return render(request, 'place-order.html')
def detail_view(request):
    # логик
    return render(request, 'product-detail.html')
def search_view(request):
    # логик
    return render(request, 'search-result.html')

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_product')  # хадгалаад дахин өөртөө орно
    else:
        form = ProductForm()

    products = Product.objects.all()  # бүх барааг авна
    return render(request, 'create_product.html', {'form': form, 'products': products})

def product_success(request):
    return render(request, 'product_success.html')

def index(request):
    cat = Category.objects.all()
    pro = Product.objects.all()
    return render(request, "index.html",{'cats':cat,'products':pro})
