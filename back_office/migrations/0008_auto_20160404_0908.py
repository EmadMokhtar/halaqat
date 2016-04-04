# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('back_office', '0007_teacher_nationality'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='nationality',
            field=models.ForeignKey(verbose_name='Nationality', blank=True, to='master_data.Nationality', null=True),
        ),
    ]
