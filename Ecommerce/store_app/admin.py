from django.contrib import admin
from .models import Category, Product
from cart_app.models import Cart,CartItem

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('category_name',)}
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('product_name',)}

admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Cart)
admin.site.register(CartItem)


