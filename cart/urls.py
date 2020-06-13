from django.urls import path

from . import views

app_name = 'cart'


urlpatterns = [
    path('', views.CartView.as_view(), name='cart'),
    path('add-item/', views.add_item, name='add-item'),
    path('remove-item/', views.remove_item, name='delete-item'),
    path('change-quantity/', views.change_item_quantity, name='change-quantity'),
]