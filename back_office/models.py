from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User

FEMALE = 'F'
MALE = 'M'


class Teacher(models.Model):
    """
    Halaqat teachers information
    """
    GENDER_CHOICES = (
        (MALE, _('Male')),
        (FEMALE, _('Female')),
    )
    gender = models.CharField(max_length=1, verbose_name=_('Gender'),
                              choices=GENDER_CHOICES)
    civil_id = models.CharField(max_length=12, verbose_name=_('Civil ID'))
    phone_number = models.CharField(max_length=15,
                                    verbose_name=_('Phone Number'))
    job_title = models.CharField(max_length=15, verbose_name=_('Title'))
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

    def get_absolute_url(self):
        return reverse('teacher_details', args=(self.pk,))


class ClassType(models.Model):
    """
    Halaqat Class Type information
    """
    name = models.CharField(max_length=20, verbose_name=_('Name'))
    monthly_fees = models.DecimalField(max_digits=6, decimal_places=3, verbose_name=_('Monthly Fees'))

    def get_absolute_url(self):
        return reverse('class_type_details', args=(self.pk,))
