# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-01 08:19
from __future__ import unicode_literals

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('back_office', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('master_data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dob', models.DateField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1, verbose_name='Gender')),
                ('civil_id', models.CharField(max_length=12, unique=True, verbose_name='Civil ID')),
                ('mobile_number', models.CharField(max_length=12, verbose_name='Mobile')),
                ('home_number', models.CharField(max_length=12, verbose_name='Home')),
                ('parent_number', models.CharField(max_length=12, verbose_name='Parents')),
                ('grade', models.CharField(blank=True, max_length=5, verbose_name='Grade')),
                ('school', models.CharField(blank=True, max_length=12, verbose_name='School')),
                ('address', models.CharField(blank=True, max_length=150, verbose_name='Address')),
                ('parent_email', models.EmailField(blank=True, max_length=254, verbose_name='Parent Email')),
                ('enrollment_date', models.DateField(null=True, verbose_name='Enrollment Date')),
                ('old_enrollment_date', models.DateField(null=True, verbose_name='Previous Center Enrollment Date')),
                ('chapter_memorized', models.IntegerField(default=0, verbose_name='Chapters Memorized')),
                ('chapter_memorized_with_center', models.IntegerField(default=0, verbose_name='Chapters memorized with center')),
                ('status', models.CharField(choices=[('P', 'Pending'), ('A', 'Active'), ('S', 'Suspended'), ('L', 'On Leave')], default='P', max_length=1, verbose_name='Status')),
                ('halaqat_class', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='back_office.HalaqatClass')),
                ('nationality', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master_data.Nationality', verbose_name='Nationality')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
