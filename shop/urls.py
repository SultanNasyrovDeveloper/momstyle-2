from django.urls import path
from . import views


urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('catalog/', views.ProductListView.as_view(), name='product_list'),
    path('catalog/<int:pk>', views.ProductDetailView.as_view(), name='product_detail'),
    path(
        'catalog/<int:pk>/quick_buy',
        views.ProductQuickBuyView.as_view(),
        name='product_quick_buy',
    ),
    path('delivery', views.Delivery.as_view(), name='delivery'),
]