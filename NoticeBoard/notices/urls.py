from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', notices, name='notices'),
    path('demo/', home, name='home'),
   
]