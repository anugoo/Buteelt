from django.db import models

class Category(models.Model):
    cname = models.CharField(max_length=100)

    def __str__(self):
        return self.cname

class Product(models.Model):
    pcategory = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    pname = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.pname} ({self.pcategory.cname})"



