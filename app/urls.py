# -*- coding:utf-8 -*-
__author__ = 'Wyc'


from django.contrib import admin
from django.urls import path, include
from app import views


urlpatterns = [

    path('upload/', views.upload),
    path('score/', views.scored),

]