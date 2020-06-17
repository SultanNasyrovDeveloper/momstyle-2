from django.urls import path

from . import views


app_name = 'favorites'

urlpatterns = [
    path('', views.FavoritesView.as_view(), name='favorites'),
    path('toggle-item/', views.toggle_item, name='toggle_item'),

]