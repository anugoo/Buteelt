from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product,Category
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
import sqlite3 


def index(request):
    pro = Product.objects.all().order_by('-created_date')[:4]
    total_count = len(pro)
    return render(request, "index.html",{'products':pro,'total': total_count})

def store_view(request):
    with sqlite3.connect("db.sqlite3") as conn:
        conn.row_factory =sqlite3.Row
        cursor= conn.cursor()
        cursor.execute("select* from store_app_product")
        pro=cursor.fetchall()
        cursor.execute("SELECT COUNT(*) FROM store_app_product")
        total_count = cursor.fetchone()[0]
    # pro = Product.objects.all()
    return render(request, "store.html",{'products': pro,'total': total_count})
def detail_view(request):
    # логик
    return render(request, 'product-detail.html')

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


