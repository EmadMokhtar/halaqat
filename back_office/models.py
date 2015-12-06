from django.db import models
from django.utils.translation import ugettext as _
from Django.contrib.auth.models import User

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
    enabled = models.BooleanField(default=True)
    user = models.OneToOneField(to=User, related_name='teacher_profile')

    def enable(self):
        """
        Enable teacher profile
        :return:
        """
        self.enabled = True
        self.save()

    def disable(self):
        """
        Disable teacher profile
        :return:
        """
        self.enabled = False
        self.save()