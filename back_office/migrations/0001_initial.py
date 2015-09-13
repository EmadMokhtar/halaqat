# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('gender', models.CharField(max_length=1, verbose_name='Gender', choices=[(b'M', 'Male'), (b'F', 'Female')])),
                ('civil_id', models.CharField(max_length=12, verbose_name='Civil ID')),
                ('phone_number', models.CharField(max_length=15, verbose_name='Phone Number')),
                ('job_title', models.CharField(max_length=15, verbose_name='Title')),
            ],
        ),
    ]
