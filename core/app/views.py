"""
Views for application app
"""
from django.shortcuts import HttpResponse


def index():
    """
    Test response
    """
    return HttpResponse("<h1>Hello, world!</h1>")
