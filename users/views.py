from django.shortcuts import render


# Create your views here.
def login(request):
    context = {
        'title': 'TechShop - Авторизация',
    }
    return render(request, 'users/login.html', context=context)

def registration(request):
    context = {
        'title': 'TechShop - Регистрация',
    }
    return render(request, 'users/registration.html', context=context)


def profile(request):
    context = {
        'title': 'TechShop - Личный кабинет',
    }
    return render(request, 'users/profile.html', context=context)

def cart(request):
    context = {
        'title': 'TechShop - Корзина',
    }
    return render(request, 'users/cart.html', context=context)


def logout(request):
    pass