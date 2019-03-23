# -*- coding:utf-8 -*-
import os
import json
from datetime import datetime
from datetime import timedelta
from django.conf import settings
from django.http import FileResponse
from django.shortcuts import render

from .models import Yeji

def download_yejiexcel(request):
    file_path = open(settings.BASE_DIR + '\\' + 'templates/admin/excel_templates/业绩导入模板.xlsx', 'rb')
    response = FileResponse(file_path, as_attachment=True)
    return response

def yejiview(request):
    date_list = []
    count_list = []
    for day in range(1, 8):
        now = datetime.now()
        dt = now - timedelta(day)
        yeji_count = Yeji.objects.filter(chujian_date__year=dt.year, chujian_date__month=dt.month,
                                         chujian_date__day=dt.day).count()
        count_list.append(yeji_count)
        date_list.append(dt.strftime('%Y-%m-%d'))

    tx_4999 = Yeji.objects.filter(taoxi='4999').count()
    tx_5999 = Yeji.objects.filter(taoxi='5999').count()
    tx_6999 = Yeji.objects.filter(taoxi='6999').count()
    tx_7999 = Yeji.objects.filter(taoxi='7999').count()
    tx_8999 = Yeji.objects.filter(taoxi='8999').count()

    context = {
        'tx_4999': tx_4999,
        'tx_5999': tx_5999,
        'tx_6999': tx_6999,
        'tx_7999': tx_7999,
        'tx_8999': tx_8999,
        'date': json.dumps(date_list),
        'count': json.dumps(count_list),
    }
    print(context)

    return render(request, 'kepan/yeji_list.html', context=context)

