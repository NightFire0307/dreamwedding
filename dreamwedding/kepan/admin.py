# -*- coding:utf-8 -*-
from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from django.contrib.admin.models import LogEntry
from daterange_filter.filter import DateRangeFilter

from .models import Kepan
from .base_admin import BaseDateTimeAdmin

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

@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ['object_repr', 'object_id', 'action_flag',
                    'user', 'change_message']