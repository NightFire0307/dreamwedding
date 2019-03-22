# -*- coding:utf-8 -*-
import os

from django.contrib import admin
from django.contrib.admin.models import LogEntry
from django.contrib.admin import helpers
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import path
from daterange_filter.filter import DateRangeFilter

from .base_admin import BaseDateTimeAdmin
from .forms import KepanExcelForms
from .models import Kepan
from .excel_save import Save_model
from .views import download_excel

@admin.register(Kepan)
class KepanAdmin(BaseDateTimeAdmin):
    list_display = ['order', 'name_man', 'name_wom',
                    'status', 'created_time']

    list_filter = (
        'status',
        ('created_time', DateRangeFilter),
    )

    list_editable = ['status']

    search_fields = ['order']

    actions_on_bottom = True
    actions_on_top = True

    save_on_top = True

    def get_urls(self):
        urls = super(KepanAdmin, self).get_urls()
        custom_urls = [
            path('upload_excel/', self.admin_site.admin_view(self.upload_excel),
                name='upload_excel'),
            path('download_excel', self.admin_site.admin_view(download_excel),
                 name='download_excel'),
        ]
        return custom_urls + urls

    def upload_excel(self, request):
        context = {
            'title': 'Upload Excel',
            'app_label': self.model._meta.app_label,
            'opts': self.model._meta,
            'has_change_permission': self.has_change_permission(request),
        }

        if request.method == 'POST':
            form = KepanExcelForms(request.POST, request.FILES)
            if form.is_valid():
                if self.is_excel(request.FILES['excel_file']):
                    Save_model(request.FILES['excel_file'])
                    return HttpResponseRedirect('..')
                else:
                    return HttpResponseRedirect('.')
        else:
            form = KepanExcelForms()

        context['form'] = form
        context['adminform'] = helpers.AdminForm(form,
                                                 list([(None, {'fields': form.base_fields})]),
                                                 {})
        return render(request, 'admin/excel/upload_excel.html', context)

    def is_excel(self, file):
        '''
        判断是否有效的Excel文件，如果有效则返回True，无效则返回False
        '''
        if os.path.splitext(str(file))[1] == '.xlsx':
            return True
        else:
            return False


@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ['object_repr', 'object_id', 'action_flag',
                    'user', 'change_message']