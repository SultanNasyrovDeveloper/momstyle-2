from django.urls import path

from . import views


urlpatterns = [
    path('', views.CartView.as_view(), name='cart'),
    # path('add-item/', test, name='add-item'),
    # path('delete-item/', delete_item, name='delete-item'),
    # path('change-quantity/', change_quantity, name='change-quantity'),
    # path('clean/', clean, name='clean'),
    # path('make-order/', make_order, name='make-order'),
]