from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from techshopapp.models import Item, User, Feedback
from .forms import CreateUserForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils import timezone
from items.models import Categories
def index(request):
    categories = Categories.objects.all()
    context = {
        'title': 'TechShop - Главная',
        'content': 'Приветствую вас в магазине техники TechShop!',
        'categories': categories
    }
    return render(request, "techshopapp/index.html", context=context)

def about(request):
    context = {
        'title': 'TechShop - О нас',
        'content': 'Здесь информация о том какой магазин классный',
        'text_on_page': 'Здесь история магазина и информация о том какой он классный'
    }
    return render(request, "techshopapp/about.html", context=context)

def contacts(request):
    context = {
        'title': 'TechShop - Контакты',
        'content': 'Здесь информация о контактах',
        'text_on_page': 'Здесь адрес и наша контанктная информация'
    }
    return render(request, "techshopapp/contacts.html", context=context)

def delivery(request):
    context = {
        'title': 'TechShop - Доставка и оплата',
        'content': 'Здесь информация о доставке и оплате',
        'text_on_page': 'Здесь подробная информация о доставке и оплате'
    }
    return render(request, "techshopapp/contacts.html", context=context)
def items_create(request):
    for i in range(20):
        item = Item.objects.create(name=f"Item_num{i}",
                                        price=12543+i,
                                        description=f"This is the coolest phone in the world num {i}",
                                        image=f"Here will be image number {i}")
        item.save()
    return HttpResponse('Create items')


def create_user_form(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreateUserForm()
    return render(request, "techshopapp/create_user_form.html", context={'form': form})


# def catalog(request):
#     items = Item.objects.all()
#     return render(request, "techshopapp/catalog.html", context={'items': items})


class ItemListView(ListView):
    model = Item
    template_name = "techshopapp/catalog.html"
    context_object_name = 'items'


class ItemDetailView(DetailView):
    model = Item
    template_name = "techshopapp/item.html"
    context_object_name = 'item'


class FeedbackListView(ListView):
    model = Feedback
    template_name = "techshopapp/feedback_list.html"
    context_object_name = 'feedback_list'


class FeedbackCreateView(CreateView):
    model = Feedback
    template_name = "techshopapp/feedback_form.html"
    fields = ['title', 'content', 'item', 'author', 'is_published', 'published_date']
    success_url = reverse_lazy('catalog')

    def form_valid(self, form):
        form.instance.is_published = True
        form.instance.published_date = timezone.now()
        return super().form_valid(form)


