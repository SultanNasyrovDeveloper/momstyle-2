from django.urls import path
from .views import Index, PostDetail, like


urlpatterns = [
    path('', Index.as_view(), name='blog'),
    path('posts/<int:post_id>', PostDetail.as_view(), name='post-detail'),
    path('like', like, name='like')
]