from django.shortcuts import render
from django.template import context

from goods.models import Product


# Create your views here.
def catalog(request):
    goods = Product.objects.all()
    context= {
        'title':'Каталог',
        'goods':goods,
    }
    return render(request, 'goods/catalog.html', context)


def product(request, product_slug):
    product= Product.objects.get(slug=product_slug)
    context={
        'product': product
    }
    return render(request, 'goods/product.html', context)

