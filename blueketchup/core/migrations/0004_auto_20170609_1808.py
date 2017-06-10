# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-09 22:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0003_auto_20170528_1959'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dish',
            name='modified_by',
        ),
        migrations.RemoveField(
            model_name='franchise',
            name='modified_by',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='modified_by',
        ),
        migrations.AddField(
            model_name='profile',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='dish',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.User'),
        ),
        migrations.AlterField(
            model_name='franchise',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='franchise',
            name='tags',
            field=models.ManyToManyField(related_name='franchise_id', to='core.Tag'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='franchise',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='franchise',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Franchise'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tag',
            name='modified_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tag_id', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]