# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-16 19:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fakturant', '0004_clientcompany_giro_account'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientcompany',
            name='giro_account',
        ),
        migrations.AddField(
            model_name='clientcompany',
            name='account',
            field=models.CharField(default='', max_length=18, verbose_name='current account'),
            preserve_default=False,
        ),
    ]
