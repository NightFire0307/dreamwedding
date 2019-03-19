# -*- coding: utf-8 -*-
# Create By:Mr.Thunder
# Power By:Abnegate
# 2019/3/19 18:21
from django.forms import forms

class KepanExcelForms(forms.Form):
    excel_file = forms.FileField(label='上传Excel文件')