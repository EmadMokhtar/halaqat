from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext as _
import json
from django.contrib.auth.models import User

GENDER_CHOICES = (
    (u'M', _(u'Male')),
    (u'F', _(u'Female')),
)

DAYS_CHOICES = (
    (u'SAT', _(u'Saturday')),
    (u'SUN', _(u'Sunday')),
    (u'MON', _(u'Monday')),
    (u'TUE', _(u'Tuesday')),
    (u'WED', _(u'Wednesday')),
    (u'Thu', _(u'Thursday')),
    (u'FRI', _(u'Friday')),
)


class Teacher(models.Model):
    """
    Halaqat teachers information
    """
    gender = models.CharField(max_length=1, verbose_name=_('Gender'),
                              choices=GENDER_CHOICES)
    civil_id = models.CharField(max_length=12, verbose_name=_('Civil ID'), unique=True)
    phone_number = models.CharField(max_length=15,
                                    verbose_name=_('Phone Number'), blank=True)
    job_title = models.CharField(max_length=15, verbose_name=_('Title'), blank=True)
    user = models.OneToOneField(to=User, related_name='teacher_profile')

    def enable(self):
        """
        Enable teacher profile
        :return:
        """
        self.user.is_active = True
        self.user.save()

    def disable(self):
        """
        Disable teacher profile
        :return:
        """
        self.user.is_active = False
        self.user.save()

    def delete(self, using=None):
        """
        Disable the teacher account instead of deleting it
        :param using:
        :return:
        """
        return self.disable()

    def get_absolute_url(self):
        return reverse('teacher-details', args=(self.pk,))

    def __str__(self):
        return u'%s %s' % (self.user.first_name, self.user.last_name)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.full_clean()
        super(Teacher, self).save(force_insert, force_update, using, update_fields)

    @property
    def full_name(self):
        return self.user.get_full_name() if self.user.get_full_name() else self.user.username


class ClassType(models.Model):
    """
    Halaqat Class Type information
    """
    name = models.CharField(max_length=20, verbose_name=_('Name'), unique=True)
    monthly_fees = models.DecimalField(max_digits=6, decimal_places=3, verbose_name=_('Monthly Fees'))

    def get_absolute_url(self):
        return reverse('class_type-details', args=(self.pk,))

    def __str__(self):
        return u'%s' % self.name


class Class(models.Model):
    """
    Halaqat Class
    """
    name = models.CharField(max_length=20, verbose_name=_('Name'))
    type = models.ForeignKey(to=ClassType, verbose_name=_('Type'), related_name='classes')
    gender = models.CharField(max_length=2, verbose_name=_('Gender'), choices=GENDER_CHOICES)
    teacher = models.ForeignKey(to=Teacher, verbose_name=_('Teacher'), related_name='classes')
    first_semester_start = models.DateField(verbose_name=_('1st Semester Start Date'))
    first_semester_end = models.DateField(verbose_name=_('1st Semester End Date'))
    second_semester_start = models.DateField(verbose_name=_('2nd Semester Start Date'))
    second_semester_end = models.DateField(verbose_name=_('2nd Semester End Date'))
    start_time = models.TimeField(verbose_name=_('Start Time'))
    end_time = models.TimeField(verbose_name=_('End Time'))
    days = models.TextField(verbose_name=_('Days'))

    def setdays(self, days):
        self.days = json.dumps(days)

    def getdays(self):
        return json.loads(self.days)

    def get_absolute_url(self):
        return reverse('class-details', args=(self.pk,))
