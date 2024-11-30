from django.urls import path
from . import views
app_name = "items"
urlpatterns = [

    path('items_create/', views.items_create, name="items_create"),
    path('<slug:category_slug>/', views.catalog, name="catalog"),
    path('<slug:category_slug>/<int:page>/', views.catalog, name="catalog"),
    path('item/<slug:item_slug>/', views.item, name="item_info"),

]

