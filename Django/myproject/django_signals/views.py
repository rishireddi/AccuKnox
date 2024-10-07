from django.http import HttpResponse
from django.shortcuts import render
from .signals import my_signal

def home(request):
    print("Home view called.")
    return HttpResponse("Hello, World!")