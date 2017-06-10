# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-09 22:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20170609_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='profiles',
            field=models.ManyToManyField(null=True, related_name='restaurant_id', to='core.Profile'),
        ),
        migrations.AlterField(
            model_name='user',
            name='profiles',
            field=models.ManyToManyField(null=True, related_name='user_id', to='core.Profile'),
        ),
    ]
