"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django_signals.views import home
from django_threading.views import threading_home
from django_db_transaction.views import transaction_home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('threading_home/', threading_home, name='threading_home'),
    path('transaction_home/', transaction_home, name='transaction_home'),
]
