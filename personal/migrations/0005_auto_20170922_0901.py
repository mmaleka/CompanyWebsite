# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-22 07:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0004_remove_signup_contact_surname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='contact_email',
            field=models.EmailField(max_length=100, unique=True),
        ),
    ]
