from django.shortcuts import render

# Create your views here.
def index(request):
    context= {
        'title':'Главная страница',
        'content':'This is CONTENT',
    }
    return render(request, 'main/index.html', context)

def about(request):
    context= {
        'title':'О нас',
        'content':'This is АБОУТ',
    }
    return render(request, 'main/about.html', context)