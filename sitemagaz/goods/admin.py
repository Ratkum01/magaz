from django.contrib import admin

# Register your models here.
from goods.models import Categories, Product
admin.site.register(Categories)
admin.site.register(Product)