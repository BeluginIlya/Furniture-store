from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {
        "title": "Главная", 
        "content": "Магазин мебели HOME"
    }
    return render(request, 'main/index.html', context)

def about(request):
    context = {
        "title": "Home - О нас", 
        "content": "О нас",
        "text_on_page": "Текст описания магазина. Просто заполняем чем-нибудь. Потом отредактирую"
    }


    return render(request, 'main/about.html', context)