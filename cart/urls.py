from django.urls import path
from .views import cart, add_item, delete_item, change_quantity, clean, make_order


urlpatterns = [
    path('', cart, name='cart'),
    path('add-item/', add_item, name='add-item'),
    path('delete-item/', delete_item, name='delete-item'),
    path('change-quantity/', change_quantity, name='change-quantity'),
    path('clean/', clean, name='clean'),
    path('make-order/', make_order, name='make-order'),
]