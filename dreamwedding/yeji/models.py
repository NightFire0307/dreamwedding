# -*- coding:utf-8 -*-
from datetime import date
from datetime import timedelta
from django.db import models
from django.utils import timezone
from django.utils.html import format_html

# class Department(models.Model):
#     name = models.CharField(max_length=30, verbose_name='订单所属部门', null=True, blank=True, unique=True)
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = verbose_name_plural = '订单所属部门'

class Shejishi(models.Model):
    STATUS_NORMAL = 0
    STATUS_QUIT = 1
    STATUS_ITEM = (
        (STATUS_NORMAL, '在职'),
        (STATUS_QUIT, '离职'),
    )

    name = models.CharField(max_length=30, verbose_name='设计师名字', default='')
    status = models.PositiveIntegerField(choices=STATUS_ITEM, default=STATUS_NORMAL, verbose_name='是否在职')

    def __str__(self):
        if self.name:
            return self.name
        else:
            return self.id

    class Meta:
        verbose_name = verbose_name_plural = '设计师'

class Yeji(models.Model):
    '''
    dealy_month 代表校稿时间往后延期一个月
    '''
    DEPARTMENT_HS = 0
    DEPARTMENT_BB = 1
    DEPARTMENT_QJF = 2
    DEPARTMENT_LF = 3

    DEPARTMENT_ITEM = (
        (DEPARTMENT_HS, '婚纱馆'),
        (DEPARTMENT_BB, '宝宝馆'),
        (DEPARTMENT_QJF, '全家福'),
    )

    delay_month = date.today() + timedelta(days=30)

    order = models.CharField(max_length=50,
                             verbose_name='订单号',
                             unique=True)
    name = models.CharField(max_length=50,
                            verbose_name='客人姓名')
    jiaogao = models.DateField(default=delay_month,
                               verbose_name='校稿日期')
    taoxi = models.IntegerField(verbose_name='套系金额')
    jiaxuan = models.IntegerField(verbose_name='加选金额',
                                  null=True,
                                  blank=True)
    owner = models.ForeignKey('Shejishi',
                              verbose_name='所属设计师',
                              on_delete=models.SET_NULL,
                              related_name='shejishi_own',
                              null=True)
    jiaogao_own = models.ForeignKey('Shejishi',
                                    verbose_name='校稿设计师',
                                    on_delete=models.SET_NULL,
                                    related_name='shejishi_jgown',
                                    null=True)
    chujian_date = models.DateField(default='',
                                    verbose_name='出件时间',
                                    null=True,
                                    blank=True)
    zhangshu = models.IntegerField(verbose_name='照片张数',
                                   null=True,
                                   blank=True)
    department = models.PositiveIntegerField(choices=DEPARTMENT_ITEM, verbose_name='订单所属部门', null=True, blank=True)
    note = models.CharField(max_length=500,
                            verbose_name='备注',
                            null=True,
                            blank=True,
                            default='')
    created_time = models.DateTimeField(auto_now=True,
                                        verbose_name='登记时间')

    def colored_chujian(self):
        return format_html(
            '<span style="color: #CC0000;">{}</span>',
            self.chujian_date
        )
    colored_chujian.short_description = '出件时间' #添加colored_chujian 描述名

    def colored_jiaogao(self):
        return format_html(
            '<span style="color: #79aec8;">{}</span>',
            self.jiaogao,
        )
    colored_jiaogao.short_description = '校稿日期'

    def __str__(self):
        if self.order:
            return '订单号：{}'.format(self.order)
        else:
            return '客户姓名：{}'.format(self.name)

    class Meta:
        ordering = ['-order']
        verbose_name = verbose_name_plural = '业绩登记表'


