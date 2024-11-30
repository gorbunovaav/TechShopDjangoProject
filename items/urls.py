from django.urls import path
from . import views
app_name = "items"
urlpatterns = [

    path('items_create/', views.items_create, name="items_create"),
    path('search/', views.catalog, name="search"),
    path('<slug:category_slug>/', views.catalog, name="catalog"),
    path('item/<slug:item_slug>/', views.item, name="item_info"),

]

