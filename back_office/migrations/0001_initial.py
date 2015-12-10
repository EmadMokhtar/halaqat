# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gender', models.CharField(max_length=1, verbose_name='Gender', choices=[(b'M', 'Male'), (b'F', 'Female')])),
                ('civil_id', models.CharField(max_length=12, verbose_name='Civil ID')),
                ('phone_number', models.CharField(max_length=15, verbose_name='Phone Number')),
                ('job_title', models.CharField(max_length=15, verbose_name='Title')),
                ('user', models.OneToOneField(related_name='teacher_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
