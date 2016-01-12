# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('back_office', '0005_auto_20151229_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='civil_id',
            field=models.CharField(unique=True, max_length=12, verbose_name='Civil ID'),
        ),
    ]
