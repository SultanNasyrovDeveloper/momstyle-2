from django.urls import path

from . import views


app_name = 'favorites'

urlpatterns = [
    path('add-item/', views.add_item, name='add_item')
]