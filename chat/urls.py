from django.shortcuts import redirect
from django.urls import path, re_path

from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('delete/', views.delete, name='delete'),
    path('message/', views.message, name='message'),
    re_path(r'^.*$', lambda request: redirect('home')),
]
