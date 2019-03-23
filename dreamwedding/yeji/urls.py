# -*- coding:utf-8 -*-
# Create By: My.Thunder
# Power By: Abnegate and Elly
# 2019/3/23 15:30

from django.urls import path

from .views import yejiview

urlpatterns = [
    path('', yejiview, name='yejiindex'),
]