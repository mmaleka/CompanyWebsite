# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-12 03:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_urladd'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to=''),
            preserve_default=False,
        ),
    ]
