# -*- coding: utf-8 -*-
# Create By:Mr.Thunder
# Power By:Abnegate
# 2019/3/26 21:54

from .base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'yeji_django',
        'USER': 'yeji',
        'PASSWORD': 'yeji',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}