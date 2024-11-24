from django.shortcuts import render
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

class ItemListView(ListView):
    model = Item
    template_name = "items/catalog.html"
    context_object_name = 'items'


class ItemDetailView(DetailView):
    model = Item
    template_name = "items/item.html"
    context_object_name = 'item'
