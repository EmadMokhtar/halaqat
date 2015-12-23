# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('back_office', '0002_classtype'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name='Name')),
                ('gender', models.CharField(max_length=2, verbose_name='Gender', choices=[(b'M', 'Male'), (b'F', 'Female')])),
                ('first_semester_start', models.DateField(verbose_name='1st Semester Start Date')),
                ('first_semester_end', models.DateField(verbose_name='1st Semester End Date')),
                ('second_semester_start', models.DateField(verbose_name='2nd Semester Start Date')),
                ('second_semester_end', models.DateField(verbose_name='2nd Semester End Date')),
                ('start_time', models.TimeField(verbose_name='Start Time')),
                ('end_time', models.TimeField(verbose_name='End Time')),
                ('days', jsonfield.fields.JSONField(verbose_name='Days', choices=[(b'SAT', 'Saturday'), (b'SUN', 'Sunday'), (b'MON', 'Monday'), (b'TUE', 'Tuesday'), (b'WED', 'Wednesday'), (b'Thu', 'Thursday'), (b'FRI', 'Friday')])),
                ('teacher', models.ForeignKey(related_name='classes', verbose_name='Teacher', to='back_office.Teacher')),
                ('type', models.ForeignKey(related_name='classes', verbose_name='Type', to='back_office.ClassType')),
            ],
        ),
    ]
