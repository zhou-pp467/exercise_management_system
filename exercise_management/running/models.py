from django.db import models
from datetime import datetime


class RunningRecord(models.Model):
    date = models.DateField(default=datetime.now, verbose_name='日期')
    speed = models.FloatField(verbose_name='速度(千米/小时)', blank=True)
    pace = models.FloatField(verbose_name='配速(分钟/千米)',blank=True)
    step_frequency = models.IntegerField(verbose_name='步频(步/分钟)')
    step_length = models.FloatField(verbose_name='步长(米/步)')
    heart_rate_average = models.IntegerField(verbose_name='平均心率(跳/分钟)')
    heart_rate_max = models.IntegerField(verbose_name='最大心率(跳/分钟)')
    memo = models.TextField(verbose_name='备注', blank=True, null=True)

    class Meta:
        verbose_name = '跑步记录'
        verbose_name_plural = '跑步记录'

    def __str__(self):
        return f'{self.date}跑步记录'