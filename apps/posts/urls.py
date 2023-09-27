from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.main_view, name='main_view'),
    path('posts/', views.posts_view, name='posts_view'),
    path('posts/<int:id>/', views.post_detail_view, name='post_detail_view'),
    path('hashtags/', views.hashtags_view, name='hashtags_view'),
]
