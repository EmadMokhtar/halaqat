from django.db import models
from django.utils.translation import ugettext as _
from master_data.models import Nationality, GENDER_CHOICES
from back_office.models import Class

PENDING = 'P'
ACTIVE = 'A'
SUSPENDED = 'S'
ON_LEAVE = 'L'

STATUS_CHOICES = (
    (PENDING, _('Pending')),
    (ACTIVE, _('Active')),
    (SUSPENDED, _('Suspended')),
    (ON_LEAVE, _('On Leave')),
    )

class Student(models.Model):
    """
    Halaqat Student
    """
    name = models.CharField(max_length=25, verbose_name=_('Name'))
    dob = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,
                              default='M', verbose_name=_('Gender'))
    civil_id = models.CharField(max_length=12, unique=True,
                                verbose_name=_('Civil ID'))
    mobile_number = models.CharField(max_length=12, verbose_name=_('Mobile'))
    home_number = models.CharField(max_length=12, verbose_name=_('Home'))
    parent_number = models.CharField(max_length=12, verbose_name=_('Parents'))
    grade = models.CharField(max_length=5, verbose_name=_('Grade'))
    school = models.CharField(max_length=12, verbose_name=_('School'))
    nationality = models.ForeignKey(Nationality, verbose_name=_('Nationality'))
    address = models.CharField(max_length=150, verbose_name=_('Address'))
    email = models.EmailField(verbose_name=_('Email'))
    parent_email = models.EmailField(verbose_name=_('Parent Email'))
    halaqat_class = models.ForeignKey(Class)
    enrollment_date = models.DateField(verbose_name=_('Enrollment Date'))
    old_enrollment_date = models.DateField(verbose_name=_('Pervious Center Enrollment Date'))
    chapter_memeorized = models.IntegerField(verbose_name=_('chapter Memeorized'))
    chapter_memeorized_with_center = models.IntegerField(verbose_name=_('chapters memeorized with center'))
    status = models.CharField(max_length=1, choices=STATUS_CHOICES,
                              default=PENDING,
                              verbose_name=_('Status'))