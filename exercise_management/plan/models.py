from django.db import models
# from exercise_type.models import StrengthTrainingType


class ExercisePlanItem(models.Model):
    date = models.DateField(verbose_name='日期')
    type = models.CharField(max_length=100, verbose_name='项目名称')
    memo = models.TextField(verbose_name='备注', blank=True, null=True)

    class Meta:
        verbose_name = '力量训练计划'
        verbose_name_plural = '力量训练计划'

    def __str__(self):
        return f'{self.date}{self.type}计划'


class RunningPlanItem(models.Model):
    date = models.DateField(verbose_name='日期')
    memo = models.TextField(verbose_name='备注', blank=True, null=True)

    class Meta:
        verbose_name = '跑步计划'
        verbose_name_plural = '跑步计划'

    def __str__(self):
        return f'{self.date}跑步计划'
