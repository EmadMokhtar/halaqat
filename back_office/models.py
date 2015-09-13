from django.db import models
from django.utils.translation import ugettext as _

FEMALE = 'F'
MALE = 'M'


class Teacher(models.Model):
    """
    halaqat teachers informations
    """
    GENDET_CHOICES = (
        (MALE, _('Male')),
        (FEMALE, _('Female')),
    )
    name = models.CharField(max_length=100, verbose_name=_('Name'))
    gender = models.CharField(max_length=1, verbose_name=_('Gender'),
                              choices=GENDET_CHOICES)
    civil_id = models.CharField(max_length=12, verbose_name=_('Civil ID'))
    phone_number = models.CharField(max_length=15,
                                    verbose_name=_('Phone Number'))
    job_title = models.CharField(max_length=15, verbose_name=_('Title'))
