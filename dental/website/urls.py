# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 15:14:29 2021

@author: karry
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('contact.html', views.contact, name="contact"),
]