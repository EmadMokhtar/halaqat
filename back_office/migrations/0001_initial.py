# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('master_data', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=20, verbose_name='Name')),
                ('monthly_fees', models.DecimalField(verbose_name='Monthly Fees', max_digits=6, decimal_places=3)),
            ],
        ),
        migrations.CreateModel(
            name='HalaqatClass',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name='Name')),
                ('gender', models.CharField(max_length=2, verbose_name='Gender', choices=[('M', 'Male'), ('F', 'Female')])),
                ('first_semester_start', models.DateField(verbose_name='1st Semester Start Date')),
                ('first_semester_end', models.DateField(verbose_name='1st Semester End Date')),
                ('second_semester_start', models.DateField(verbose_name='2nd Semester Start Date')),
                ('second_semester_end', models.DateField(verbose_name='2nd Semester End Date')),
                ('start_time', models.TimeField(verbose_name='Start Time')),
                ('end_time', models.TimeField(verbose_name='End Time')),
                ('days', models.TextField(verbose_name='Days')),
                ('class_type', models.ForeignKey(related_name='classes', verbose_name='Type', to='back_office.ClassType')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gender', models.CharField(max_length=1, verbose_name='Gender', choices=[('M', 'Male'), ('F', 'Female')])),
                ('civil_id', models.CharField(unique=True, max_length=12, verbose_name='Civil ID')),
                ('phone_number', models.CharField(max_length=15, verbose_name='Phone Number', blank=True)),
                ('job_title', models.CharField(max_length=15, verbose_name='Title', blank=True)),
                ('nationality', models.ForeignKey(verbose_name='Nationality', blank=True, to='master_data.Nationality', null=True)),
                ('user', models.OneToOneField(related_name='teacher_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='halaqatclass',
            name='teacher',
            field=models.ForeignKey(related_name='classes', verbose_name='Teacher', to='back_office.Teacher'),
        ),
    ]
