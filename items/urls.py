from django.urls import path
from . import views
app_name="items"
urlpatterns = [

    path('items_create/', views.items_create, name="items_create"),
    # path('contacts/', views.contacts, name="contacts"),
    path('', views.ItemListView.as_view(), name="catalog"),
    path('item_info/<int:pk>/', views.ItemDetailView.as_view(), name="item_info"),

]

