# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('back_office', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('master_data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dob', models.DateField()),
                ('gender', models.CharField(default=b'M', max_length=1, verbose_name='Gender', choices=[('M', 'Male'), ('F', 'Female')])),
                ('civil_id', models.CharField(unique=True, max_length=12, verbose_name='Civil ID')),
                ('mobile_number', models.CharField(max_length=12, verbose_name='Mobile')),
                ('home_number', models.CharField(max_length=12, verbose_name='Home')),
                ('parent_number', models.CharField(max_length=12, verbose_name='Parents')),
                ('grade', models.CharField(max_length=5, verbose_name='Grade', blank=True)),
                ('school', models.CharField(max_length=12, verbose_name='School', blank=True)),
                ('address', models.CharField(max_length=150, verbose_name='Address', blank=True)),
                ('parent_email', models.EmailField(max_length=254, verbose_name='Parent Email', blank=True)),
                ('enrollment_date', models.DateField(null=True, verbose_name='Enrollment Date')),
                ('old_enrollment_date', models.DateField(null=True, verbose_name='Previous Center Enrollment Date')),
                ('chapter_memorized', models.IntegerField(default=0, verbose_name='Chapters Memorized')),
                ('chapter_memorized_with_center', models.IntegerField(default=0, verbose_name='Chapters memorized with center')),
                ('status', models.CharField(default=b'P', max_length=1, verbose_name='Status', choices=[(b'P', 'Pending'), (b'A', 'Active'), (b'S', 'Suspended'), (b'L', 'On Leave')])),
                ('halaqat_class', models.ForeignKey(blank=True, to='back_office.HalaqatClass', null=True)),
                ('nationality', models.ForeignKey(verbose_name='Nationality', blank=True, to='master_data.Nationality', null=True)),
                ('user', models.ForeignKey(related_name='student_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
