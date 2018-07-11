# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-10 14:05
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainapp', '0010_auto_20180710_1539'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='author',
        ),
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.AddField(
            model_name='comment',
            name='uploadedby',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='Categorization',
            field=models.CharField(choices=[('', '--'), ('B', 'biology'), ('M', 'microbiology'), ('P', 'physiology')], default=True, max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='uploadedby',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
