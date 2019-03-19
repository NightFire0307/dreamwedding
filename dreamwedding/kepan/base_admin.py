# -*- coding:utf-8 -*-
# Create By: My.Thunder
# Power By: Abnegate and Elly
# 2019/3/19 16:21
from datetime import datetime
from django.contrib import admin

class BaseDateTimeAdmin(admin.ModelAdmin):
    exclude = ('created_time', )

    def save_model(self, request, obj, form, change):
        obj.created_time = datetime.now()
        return super(BaseDateTimeAdmin, self).save_model(request, obj, form, change)

