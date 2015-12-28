# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('back_office', '0003_class'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='days',
            field=models.TextField(verbose_name='Days'),
        ),
        migrations.AlterField(
            model_name='classtype',
            name='name',
            field=models.CharField(unique=True, max_length=20, verbose_name='Name'),
        ),
    ]
