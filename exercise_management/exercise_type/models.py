from django.db import models
from datetime import datetime


# class StrengthTrainingType(models.Model):
#     name = models.CharField(unique=True, max_length=100, verbose_name='项目名称')
#
#     class Meta:
#         verbose_name = '项目列表'
#         verbose_name_plural = '项目列表'
#
#     def __str__(self):
#         return self.name


class StrengthTrainingRecord(models.Model):
    date = models.DateField(default=datetime.now, verbose_name='日期')
    type = models.CharField(max_length=100, verbose_name='项目名称')
    weight = models.FloatField(verbose_name='重量(千克)')
    repeat_times = models.IntegerField(verbose_name='重复次数')
    memo = models.TextField(verbose_name='备注', blank=True, null=True)

    class Meta:
        verbose_name = '健身记录'
        verbose_name_plural = '健身记录'

    def __str__(self):
        return self.type
