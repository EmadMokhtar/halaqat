# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('back_office', '0004_auto_20151228_0749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='job_title',
            field=models.CharField(max_length=15, verbose_name='Title', blank=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='phone_number',
            field=models.CharField(max_length=15, verbose_name='Phone Number', blank=True),
        ),
    ]
