from django.urls import path
from . import views
app_name="items"
urlpatterns = [

    path('items_create/', views.items_create, name="items_create"),
    # path('contacts/', views.contacts, name="contacts"),
    path('', views.catalog, name="catalog"),
    path('item_info/<int:pk>/', views.item, name="item_info"),

]

