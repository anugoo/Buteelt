from .models import *
from cart_app.models import CartItem,Cart
from  cart_app.views import _cart_id

def category_processor(request):
    categories = Category.objects.all()  
    return {'all_categories': categories}  
def cart_processor(request):
    cart_count = 0
    if 'admin' in request.path:
        return {}
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart_id=cart)
        for item in cart_items:
            cart_count += item.quantity
    except Cart.DoesNotExist:
        cart_count = 0
    return {'cart_total': cart_count}