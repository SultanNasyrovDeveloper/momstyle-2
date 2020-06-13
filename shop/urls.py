from django.urls import path
from .views import (Index, Catalog, Delivery, ProductDetailView, contact_us)
from . import views


urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('catalog/', views.ProductListView.as_view(), name='product_list'),
    path('catalog/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('delivery', Delivery.as_view(), name='delivery'),
    path('contact-us', contact_us, name='contact-us')
]