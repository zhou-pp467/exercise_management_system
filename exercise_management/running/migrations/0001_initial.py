# Generated by Django 3.2.9 on 2022-03-08 13:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RunningRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.datetime.now, verbose_name='日期')),
                ('speed', models.FloatField(verbose_name='速度')),
                ('pace', models.FloatField(verbose_name='配速')),
                ('step_frequency', models.FloatField(verbose_name='步频')),
                ('step_length', models.FloatField(verbose_name='步长')),
                ('heart_rate_average', models.FloatField(verbose_name='平均心率')),
                ('heart_rate_max', models.FloatField(verbose_name='最大心率')),
            ],
            options={
                'verbose_name': '跑步记录',
                'verbose_name_plural': '跑步记录',
            },
        ),
    ]
