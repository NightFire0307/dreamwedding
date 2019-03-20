# -*- coding: utf-8 -*-
# Create By:Mr.Thunder
# Power By:Abnegate
# 2019/3/20 18:03

from django.urls import path

from .views import IndexView

urlpatterns = [
    path('', IndexView, name='indexview'),
]