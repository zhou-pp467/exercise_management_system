# Generated by Django 3.2.9 on 2022-03-10 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercise_type', '0003_auto_20220310_1445'),
    ]

    operations = [
        migrations.AddField(
            model_name='strengthtrainingrecord',
            name='memo',
            field=models.TextField(blank=True, null=True, verbose_name='备注'),
        ),
    ]
