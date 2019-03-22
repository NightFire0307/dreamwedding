# -*- coding:utf-8 -*-
from django.contrib import admin
from daterange_filter.filter import DateRangeFilter

from .models import Shejishi, Yeji

@admin.register(Shejishi)
class ShejishiAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Yeji)
class YejiAdmin(admin.ModelAdmin):
    list_display = ['order', 'name', 'jiaogao',
                    'taoxi', 'jiaxuan', 'owner',
                    'jiaogao_own', 'chujian_date', 'zhangshu',
                    'note', 'created_time']

    list_filter = ('owner', 'jiaogao_own',
                   ('chujian_date', DateRangeFilter),
                   ('created_time', DateRangeFilter))
    # list_editable = ['chujian_date']

    save_on_top = True
    actions_on_top = True
    actions_on_bottom = True
    search_fields = ['order', 'jiaogao_own__name']

