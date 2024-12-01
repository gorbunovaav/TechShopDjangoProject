from django.shortcuts import render, redirect
from django.http import HttpResponse
from techshopapp.models import Item, Feedback
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.utils import timezone


def index(request):

    context = {
        'title': 'TechShop - Главная',
        'content': 'Приветствую вас в магазине техники TechShop!',
    }
    return render(request, "techshopapp/index.html", context=context)

def about(request):
    context = {
        'title': 'TechShop - О нас',
        'content': 'Здесь информация о том какой магазин классный',
        'text_on_page': 'Здесь история магазина и информация о том какой он классный Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
    }
    return render(request, "techshopapp/about.html", context=context)

def contacts(request):
    context = {
        'title': 'TechShop - Контакты',
        'content': 'Здесь информация о контактах',
        'text_on_page': 'Москва, Россия, Адрес'
                        'techshop@example.com'
                        '+ 055588373772'
    }
    return render(request, "techshopapp/contacts.html", context=context)

def delivery(request):
    context = {
        'title': 'TechShop - Доставка и оплата',
        'content': 'Здесь информация о доставке и оплате',
        'text_on_page': 'Доставка осуществляется курьерской службой СДЭК. Детальные условия доставки в Ваш город (стоимость, сроки, оплата) и возможность использовать альтернативные варианты (Почта России, курьерская служба Яндекс, EMS) можно узнать непосредственно у оператора интернет-магазина, при подтверждении заказа. Заказы по г. Новосибирску и г. Бердску доставляются, в рабочие дни с 10:00 до 18:00, отправка заказа происходит на следующий день после подтверждения оператором интернет-магазина. При сумме заказа меньше 5 000 рублей стоимость доставки – 550 руб. В выходные и праздничные дни доставка не осуществляется. Самостоятельно забрать заказы в г. Новосибирск можно c 09:00-21:00, перерывы 12:30-13:00, 16:30-17:00, без выходных, в офисе по адресу ул. Коммунистическая, 35. Заказ доставляется в офис на следующий рабочий день после подтверждения оператором интернет-магазина и оплаты заказа на сайте. '
                        'Заказы по г. Москва (в пределах МКАД) доставляются курьером, на следующий рабочий день после подтверждения оператором интернет-магазина и оплаты заказа на сайте. При сумме заказа меньше 5 000 рублей стоимость доставки – 550 руб. Если Вы хотите оплатить заказ при получении, то заказ будет доставлен в течение 3-7 рабочих дней. В выходные и праздничные дни доставка не осуществляется.'}
    return render(request, "techshopapp/delivery.html", context=context)
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


# class ItemListView(ListView):
#     model = Item
#     template_name = "techshopapp/catalog.html"
#     context_object_name = 'items'


# class ItemDetailView(DetailView):
#     model = Item
#     template_name = "techshopapp/item.html"
#     context_object_name = 'item'


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


