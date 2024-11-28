from django.db.models import QuerySet
from django.shortcuts import render
from .forms import UserRegister
from .models import *


# Create your views here.


def platform(request):
    title = 'Главная страница'
    context = {
        'title': title
    }
    return render(request, 'platform.html', context)


def games(request):
    game_list = Game.objects.all()
    title = 'Игры'
    context = {
        'title': title,
        'game_list': game_list
    }
    return render(request, 'games.html', context)


def cart(request):
    title = 'Корзина'
    context = {
        'title': title
    }
    return render(request, 'cart.html', context)


buyers = Buyer.objects.all()


def sign_up_by_html(request):
    info = {}
    if request.method == "POST":
        username = request.POST.get('username')
        balance = request.POST.get('balance')
        age = request.POST.get('age')
        if float(balance) < 0:
            info['error'] = 'Баланс не может быть отрицательным!'
        elif username in [buyer.name for buyer in buyers]:
            info['error'] = 'Пользователь уже существует'
        else:
            info['message'] = f'Приветствуем, {username}!'
            Buyer.objects.create(name = username,
                                 balance=float(balance),
                                 age=int(age))
    return render(request, 'registration_page.html', info)


def sign_up_by_django(request):
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            balance = form.cleaned_data['balance']
            age = form.cleaned_data['age']
            if float(balance) < 0:
                info['error'] = 'Баланс не может быть отрицательным!'
            elif username in [buyer.name for buyer in buyers]:
                info['error'] = 'Пользователь уже существует'
            else:
                info['message'] = f'Приветствуем, {username}!'
                Buyer.objects.create(name=username,
                                     balance=float(balance),
                                     age=int(age))
    return render(request, 'registration_page.html', info)
