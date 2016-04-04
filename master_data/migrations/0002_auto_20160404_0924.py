# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master_data', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nationality',
            name='name',
            field=models.CharField(unique=True, max_length=10, verbose_name='Name'),
        ),
    ]
