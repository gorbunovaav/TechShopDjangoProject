from django.shortcuts import render, get_list_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from items.models import Item


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
    if category_slug == 'all':
        items = Item.objects.all()
    else:
        items = get_list_or_404(Item.objects.filter(category__slug=category_slug))

    context = {
        'title': 'TechShop - Каталог',
        'items': items,
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
