from django.urls import path
from .views import cart,add_to_cart,remove_from_cart, decrease_quantity


urlpatterns = [
    path('', cart, name='cart'),
    path('add/<int:product_id>/', add_to_cart, name='add_cart'),
    path('remove/<int:product_id>/', decrease_quantity, name='remove_cart'),
    path('remove_item/<int:product_id>/', remove_from_cart, name='remove_cart_item'),
]
