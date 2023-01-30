"""
Urls patterns for application app
"""
from django.urls import path
from .views import index


urlpatterns = [
    path('', index, name='index'),
]
