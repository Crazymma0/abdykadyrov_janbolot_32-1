from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_view, name='hello'),
    path('now_date/', views.now_date_view, name='now_date'),
    path('goodby/', views.goodby_view, name='goodbye'),
]
