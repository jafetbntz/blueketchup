# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-09 23:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20170609_1843'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='franchise',
            options={'verbose_name': 'Franquicia', 'verbose_name_plural': 'Franquicias'},
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'Perfil', 'verbose_name_plural': 'Perfiles'},
        ),
        migrations.RemoveField(
            model_name='dish',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='dish',
            name='updated_date',
        ),
        migrations.RemoveField(
            model_name='franchise',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='franchise',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='franchise',
            name='updated_date',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='updated_date',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='updated_date',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='modified_by',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='updated_date',
        ),
    ]