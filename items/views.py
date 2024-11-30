from django.shortcuts import render, get_list_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from items.models import Item
from django.core.paginator import Paginator


#     return render()
#
# def item(request):
#     return render()

def items_create(request):
    for i in range(20):
        item = Item.objects.create(name=f"Item_num{i}",
                                        price=12543+i,
                                        description=f"This is the coolest phone in the world num {i}",
                                        image=f"Here will be image number {i}")
        item.save()
    return HttpResponse('Create items')


def catalog(request, category_slug):
    page = request.GET.get('page', 1)
    on_sale = request.GET.get('on_sale', None)
    order_by = request.GET.get('order_by', None)

    if category_slug == 'all':
        items = Item.objects.all()
    else:
        items = get_list_or_404(Item.objects.filter(category__slug=category_slug))

    if on_sale:
        items = items.filter(discount__gt=0)

    if order_by and order_by != 'default':
        items = items.order_by(order_by)

    paginator = Paginator(items, 6)
    current_page = paginator.page(int(page))
    context = {
        'title': 'TechShop - Каталог',
        'items': current_page,
        'slug_url': category_slug,
    }
    return render(request, 'items/catalog.html', context=context)

def item(request, item_slug):

    item = Item.objects.get(slug=item_slug)
    context = {
        'item': item,
    }
    return render(request, 'items/item.html', context=context)
# class ItemListView(ListView):
#     model = Item
#     template_name = "items/catalog.html"
#     context_object_name = 'items'


# class ItemDetailView(DetailView):
#     model = Item
#     template_name = "items/item.html"
#     context_object_name = 'item'
