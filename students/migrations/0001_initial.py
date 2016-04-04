# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master_data', '0001_initial'),
        ('back_office', '0007_teacher_nationality'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=25, verbose_name='Name')),
                ('dob', models.DateField()),
                ('gender', models.CharField(default=b'M', max_length=1, verbose_name='Gender', choices=[('M', 'Male'), ('F', 'Female')])),
                ('civil_id', models.CharField(unique=True, max_length=12, verbose_name='Civil ID')),
                ('mobile_number', models.CharField(max_length=12, verbose_name='Mobile')),
                ('home_number', models.CharField(max_length=12, verbose_name='Home')),
                ('parent_number', models.CharField(max_length=12, verbose_name='Parents')),
                ('grade', models.CharField(max_length=5, verbose_name='Grade')),
                ('school', models.CharField(max_length=12, verbose_name='School')),
                ('address', models.CharField(max_length=150, verbose_name='Address')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('parent_email', models.EmailField(max_length=254, verbose_name='Parent Email')),
                ('enrollment_date', models.DateField(verbose_name='Enrollment Date')),
                ('old_enrollment_date', models.DateField(verbose_name='Pervious Center Enrollment Date')),
                ('chapter_memeorized', models.IntegerField(verbose_name='chapter Memeorized')),
                ('chapter_memeorized_with_center', models.IntegerField(verbose_name='chapters memeorized with center')),
                ('status', models.CharField(default=b'P', max_length=1, verbose_name='Status', choices=[(b'P', 'Pending'), (b'A', 'Active'), (b'S', 'Suspended'), (b'L', 'On Leave')])),
                ('halaqat_class', models.ForeignKey(to='back_office.Class')),
                ('nationality', models.ForeignKey(verbose_name='Nationality', to='master_data.Nationality', null=True)),
            ],
        ),
    ]
