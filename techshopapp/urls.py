from django.urls import path
from . import views
app_name="techshop"
urlpatterns = [
    path('home/', views.index, name="home"),
    path('about/', views.about, name="about"),
    path('contacts/', views.contacts, name="contacts"),
    path('delivery/', views.delivery, name="delivery"),
    # path('items_create/', views.items_create, name="items_create"),
    # path('contacts/', views.contacts, name="contacts"),
    # path('catalog/', views.ItemListView.as_view(), name="catalog"),
    path('registration_form/', views.create_user_form, name="create_user_form"),
    # path('item_info/<int:pk>/', views.ItemDetailView.as_view(), name="item_info"),
    path('feedback_list/', views.FeedbackListView.as_view(), name="feedback_list"),
    path('feedback/new/', views.FeedbackCreateView.as_view(), name="feedback_create"),

]

