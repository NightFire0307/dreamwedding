# -*- coding:utf-8 -*-
import os
import json
from datetime import datetime
from datetime import timedelta
from django.conf import settings
from django.http import FileResponse
from django.shortcuts import render

from .models import Yeji, Shejishi

def download_yejiexcel(request):
    file_path = open(settings.BASE_DIR + '\\' + 'templates/admin/excel_templates/业绩导入模板.xlsx', 'rb')
    response = FileResponse(file_path, as_attachment=True)
    return response

def yejiview(request):
    owner_all = list(Shejishi.objects.filter(status=Shejishi.STATUS_NORMAL))
    owner_name = [name.name for name in owner_all]
    owner_id_list = [name.id for name in owner_all]
    owner_out_count = []

    for owner in owner_id_list:
        owner_out_count.append(Yeji.objects.filter(owner_id=owner, chujian_date__month=datetime.now().month).count())

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
        'owner': json.dumps(owner_name),
        'owner_count': json.dumps(owner_out_count),
    }

    return render(request, 'kepan/yeji_list.html', context=context)

