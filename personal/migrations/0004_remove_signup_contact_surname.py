# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-19 00:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0003_signup'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signup',
            name='contact_surname',
        ),
    ]