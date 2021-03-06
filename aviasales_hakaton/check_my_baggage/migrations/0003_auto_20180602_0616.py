# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-02 06:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('check_my_baggage', '0002_auto_20180602_0556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airlinecompany',
            name='icon',
            field=filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='icon', to=settings.FILER_IMAGE_MODEL, verbose_name='Logo icon 50x50'),
        ),
        migrations.AlterField(
            model_name='airlinecompany',
            name='logo',
            field=filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='logo', to=settings.FILER_IMAGE_MODEL, verbose_name='Logo image [large]'),
        ),
    ]
