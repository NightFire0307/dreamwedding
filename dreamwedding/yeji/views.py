# -*- coding:utf-8 -*-
import os
from django.conf import settings
from django.http import FileResponse
from django.shortcuts import render

def download_yejiexcel(request):
    file_path = open(settings.BASE_DIR + '\\' + 'templates/admin/excel_templates/业绩导入模板.xlsx', 'rb')
    response = FileResponse(file_path, as_attachment=True)
    return response

