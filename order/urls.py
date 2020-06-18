from django.urls import path

from . import views

app_name = 'order'


urlpatterns = [
    path('checkout/personal', views.OrderPersonalInfoCheckoutView.as_view(), name='personal_info'),
    path('checkout/delivery', views.OrderDeliveryCheckoutView.as_view(), name='delivery'),
    path('checkout/payment', views.OrderPaymentCheckoutView.as_view(), name='payment'),
    path('checkout', views.OrderCheckoutView.as_view(), name='checkout'),
    path('checkout/redirect', views.redirect_to_form, name='redirect'),
    path('<int:pk>/checkout/complete', views.CheckoutCompleteView.as_view(), name='complete'),
]