# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-25 18:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20170525_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
