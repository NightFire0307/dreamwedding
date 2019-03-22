# -*- coding:utf-8 -*-
import os
from django.contrib import admin
from django.contrib.admin import helpers
from django.http import HttpResponseRedirect
from django.urls import path
from django.shortcuts import render
from daterange_filter.filter import DateRangeFilter

from .models import Shejishi, Yeji

from kepan.forms import ExcelForms
from kepan.admin import is_excel
from .excel_save import Save_yejimodel

@admin.register(Shejishi)
class ShejishiAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Yeji)
class YejiAdmin(admin.ModelAdmin):
    list_display = ['order', 'name', 'colored_jiaogao',
                    'taoxi', 'jiaxuan', 'owner',
                    'jiaogao_own', 'colored_chujian', 'zhangshu',
                    'note', 'created_time']

    list_filter = ('owner', 'jiaogao_own',
                   ('chujian_date', DateRangeFilter),
                   ('created_time', DateRangeFilter),)
    # list_editable = ['chujian_date']

    save_on_top = True
    actions_on_top = True
    actions_on_bottom = True
    search_fields = ['order', 'jiaogao_own__name']

    def get_urls(self):
        urls = super(YejiAdmin, self).get_urls()
        custom_urls = [
            path('upload_yejiexcel', self.admin_site.admin_view(self.upload_yejiexcel),
                 name='upload_yejiexcel'),
        ]
        return custom_urls + urls

    def upload_yejiexcel(self, request):
        context = {
            'title': 'Upload Excel',
            'app_label': self.model._meta.app_label,
            'opts': self.model._meta,
            'has_change_permission': self.has_change_permission(request),
        }

        if request.method == 'POST':
            form = ExcelForms(request.POST, request.FILES)
            if form.is_valid():
                if is_excel(request.FILES['excel_file']):
                    Save_yejimodel(request.FILES['excel_file'])
                    return HttpResponseRedirect('.')
                else:
                    return HttpResponseRedirect('.')
        else:
            form = ExcelForms()

        context['form'] = form
        context['adminform'] = helpers.AdminForm(form,
                                                 list([(None, {'fields': form.base_fields})]),
                                                 {})
        return render(request, 'admin/excel/upload_yejiexcel.html', context)

