# cors_proxy/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('proxy/', views.proxy_view, name='proxy'),
]

