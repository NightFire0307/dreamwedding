# -*- coding:utf-8 -*-
import os
import json
from datetime import datetime
from datetime import timedelta
from django.conf import settings
from django.http import FileResponse
from django.shortcuts import render

from .models import Kepan

def download_excel(request):
    file_path = open(settings.BASE_DIR + '\\' + 'templates/admin/excel_templates/刻盘导入模板.xlsx', 'rb')
    response = FileResponse(file_path, as_attachment=True)
    return response

def IndexView(request):
    date_list = []
    count_list = []
    for day in range(1, 8):
        now = datetime.now()
        dt = now - timedelta(day)
        kepan_count = Kepan.objects.filter(created_time__year=dt.year,
                                           created_time__month=dt.month,
                                           created_time__day=dt.day).count()
        count_list.append(kepan_count)
        date_list.append(dt.strftime('%Y-%m-%d'))

    context = {
        'date': json.dumps(date_list),
        'count': json.dumps(count_list),
    }
    return render(request, 'kepan/index.html', context=context)