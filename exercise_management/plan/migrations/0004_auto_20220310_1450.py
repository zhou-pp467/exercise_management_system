# Generated by Django 3.2.9 on 2022-03-10 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0003_alter_exerciseplanitem_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='exerciseplanitem',
            name='memo',
            field=models.TextField(blank=True, null=True, verbose_name='备注'),
        ),
        migrations.AddField(
            model_name='runningplanitem',
            name='memo',
            field=models.TextField(blank=True, null=True, verbose_name='备注'),
        ),
    ]
