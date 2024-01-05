from django.shortcuts import render

from goods.models import Categories

# Create your views here.
def index(request):
    categories= Categories.objects.all()
    context= {
        'title':'Главная страница',
        'content':'This is CONTENT',
        'categories':categories
    }
    return render(request, 'main/index.html', context)

def about(request):
    context= {
        'title':'О нас',
        'content':'This is АБОУТ',
    }
    return render(request, 'main/about.html', context)