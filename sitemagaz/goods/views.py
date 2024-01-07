from django.shortcuts import render

from goods.models import Product


# Create your views here.
def catalog(request):
    goods = Product.objects.all()
    context= {
        'title':'Каталог',
        'goods':goods,
    }
    return render(request, 'goods/catalog.html', context)


def product(request):
    return render()

