# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master_data', '0001_initial'),
        ('back_office', '0006_auto_20160111_1315'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='nationality',
            field=models.ForeignKey(verbose_name='Nationality', to='master_data.Nationality', null=True),
        ),
    ]
