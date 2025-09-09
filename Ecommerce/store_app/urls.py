from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product/create/', views.create_product, name='create_product'),
    path('product/success/', views.product_success, name='product_success'),
    path('signin/', views.signin_view, name='signin'),
    path('register/', views.register_view, name='register'),
    path('store/', views.store_view, name='store'),
    path('cart/', views.cart_view, name='cart'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('order/', views.order_view, name='order'),
    path('place/', views.place_view, name='place'),
    path('detail/', views.detail_view, name='detail'),
    path('search/', views.search_view, name='search'),
      # амжилтын хуудсанд шилжих
]
