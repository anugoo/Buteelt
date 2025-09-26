from .models import Category

def category_processor(request):
    categories = Category.objects.all()  # Бүх category-г авна
    return {'all_categories': categories}  # template-д дамжуулна