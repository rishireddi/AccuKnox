from django.http import HttpResponse
from django.shortcuts import render
from .threading import my_threading_signal
import threading

def threading_home(request):
    print(f"Home view called in thread: {threading.get_ident()}")
    my_threading_signal.send(sender='home_view')
    return HttpResponse("Threading In Django")