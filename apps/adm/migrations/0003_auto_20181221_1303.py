# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-12-21 13:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adm', '0002_auto_20181221_1136'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='assettype',
            options={'verbose_name': '资产类型', 'verbose_name_plural': '资产类型'},
        ),
        migrations.AddField(
            model_name='assettype',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='adm.AssetType', verbose_name='父类资产'),
        ),
    ]
