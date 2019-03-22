# -*- coding:utf-8 -*-
# Create By: My.Thunder
# Power By: Abnegate and Elly
# 2019/3/19 16:21
from datetime import date
from django.contrib import admin

class BaseDateTimeAdmin(admin.ModelAdmin):
    '''
    Admin 自动添加时间基类
    '''
    # exclude = ('created_time', )

    def save_model(self, request, obj, form, change):
        obj.created_time = date.today()
        return super(BaseDateTimeAdmin, self).save_model(request, obj, form, change)

