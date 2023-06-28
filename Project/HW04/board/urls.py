from django.urls import re_path as url, include
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
] 