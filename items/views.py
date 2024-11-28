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

def catalog(request):
    context = {
        'title': 'TechShop - Каталог',
        'items': [
        {'name': 'Iphone',
         'description': 'The best phone',
         'price': '1434',
         'image': 'No image'
         },
        {'name': 'Iphone2',
         'description': 'The best phone',
         'price': '1434',
         'image': 'No image'
         },
        {'name': 'Iphone3',
         'description': 'The best phone',
         'price': '1434',
         'image': 'No image'
         },
        {'name': 'Iphone4',
         'description': 'The best phone',
         'price': '1434',
         'image': 'No image'
         },
        {'name': 'Iphone5',
         'description': 'The best phone',
         'price': '1434',
         'image': 'No image'
         },
        {'name': 'Iphone6',
         'description': 'The best phone',
         'price': '1434',
         'image': 'No image'
         },
        {'name': 'Iphone7',
         'description': 'The best phone',
         'price': '1434',
         'image': 'No image'
         },
        {'name': 'Iphone8',
         'description': 'The best phone',
         'price': '1434',
         'image': 'No image'
         },
        {'name': 'Iphone9',
         'description': 'The best phone',
         'price': '1434',
         'image': 'No image'
         },
    ]
    }
    return render(request, 'items/catalog.html', context=context)

def item(request):
    return render(request, 'items/item.html')
# class ItemListView(ListView):
#     model = Item
#     template_name = "items/catalog.html"
#     context_object_name = 'items'


# class ItemDetailView(DetailView):
#     model = Item
#     template_name = "items/item.html"
#     context_object_name = 'item'
