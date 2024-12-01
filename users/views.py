from django.shortcuts import render
from users.forms import UserLoginForm, CreateUserForm
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect



# Create your views here.
def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('techshop:home'))
    else:
        form = UserLoginForm()

    context = {
        'title': 'TechShop - Авторизация',
        'form': form,
    }
    return render(request, 'users/login.html', context)

def registration(request):
    if request.method == 'POST':
        form = CreateUserForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            return HttpResponseRedirect(reverse('techshop:home'))
    else:
        form = CreateUserForm()
    context = {
        'title': 'TechShop - Регистрация',
        'form': form,
    }
    return render(request, 'users/registration.html', context)


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
    auth.logout(request)
    return redirect(reverse('techshop:home'))