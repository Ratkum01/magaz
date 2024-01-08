from django.shortcuts import get_object_or_404, render
from django.template import context

from goods.models import Product


# Create your views here.
def catalog(request, category_slug):
    if category_slug == 'vse-tovary':
        goods = Product.objects.all()
    else:
        goods = get_object_or_404(Product.objects.filter(category__slug=category_slug))

    context = {
        'title': 'Каталог',
        'goods': goods,
    }

    return render(request, 'goods/catalog.html', context)



def product(request, product_slug):
    product= Product.objects.get(slug=product_slug)
    context={
        'product': product
    }
    return render(request, 'goods/product.html', context)

