from django.urls import path
from . import views
app_name = "items"
urlpatterns = [

    path('items_create/', views.items_create, name="items_create"),
    # path('contacts/', views.contacts, name="contacts"),
    path('<slug:category_slug>/', views.catalog, name="catalog"),
    path('item/<slug:item_slug>/', views.item, name="item_info"),

]

