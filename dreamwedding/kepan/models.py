# -*- coding:utf-8 -*-
from django.db import models

class Kepan(models.Model):
    STATUS_UNFINASHED = 0
    STATUS_FINASH = 1
    STATUS_ITEM = (
        (STATUS_UNFINASHED, '未完成'),
        (STATUS_FINASH, '已完成'),
    )

    order = models.CharField(max_length=10, verbose_name='订单号', unique=True)
    name_man = models.CharField(max_length=50, verbose_name='先生姓名', null=True, blank=True)
    name_wom = models.CharField(max_length=50, verbose_name='小姐姓名', null=True, blank=True)
    status = models.PositiveIntegerField(choices=STATUS_ITEM, default=STATUS_UNFINASHED, verbose_name='刻盘状态')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    note = models.CharField(max_length=500, verbose_name='备注', null=True, blank=True)

    def __str__(self):
        return self.order

    class Meta:
        verbose_name = verbose_name_plural = '刻盘记录'


