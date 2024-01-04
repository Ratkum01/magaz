from django.shortcuts import render


# Create your views here.
def catalog(request):
    context= {
        'title':'Главная страница',
        'content':'This is CONTENT',
    }
    return render(request, 'goods/catalog.html')


def product(request):
    return render()
