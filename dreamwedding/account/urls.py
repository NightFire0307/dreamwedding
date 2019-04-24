# -*- coding:utf-8 -*-
# Create By: My.Thunder
# Power By: YuXiaoyu
# 2019/4/24 12:19

from django.urls import path

from .views import user_login, user_logout

urlpatterns = [
    path('', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]