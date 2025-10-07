from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path("store/", views.store_view, name="store"),
    # path('store/<slug:category_slug>/<slug:product_slug>/', views.store_view_detail, name='detail'),
    path('<slug:category_slug>/', views.store_view_detail, name='store_by_category'),
    path('<slug:category_slug>/<slug:product_slug>/', views.store_view_detail, name='detail'),
    # path('store/<slug:category_slug>/<slug:product_slug>/', views.store_view_detail, name='detail1'),
    path('product/create/', views.create_product, name='create_product'),
    path('product/success/', views.product_success, name='product_success'),
    path('signin/', views.signin_view, name='signin'),
    path('register/', views.register_view, name='register'),
    path('cart/', views.cart_view, name='cart'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('order/', views.order_view, name='order'),
    path('place/', views.place_view, name='place'),
    path('search/', views.search_view, name='search'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
