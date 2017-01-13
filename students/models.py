import operator
from functools import reduce

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models import Q
from django.utils.translation import ugettext_lazy as _

from back_office.models import HalaqatClass
from master_data.models import GENDER_CHOICES, Nationality

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


class StudnetManager(models.Manager):

    def search(self, search_terms):
        terms = [term.strip() for term in search_terms.split()]
        q_objects = []

        for term in terms:
            q_objects.append(Q(civil_id__icontains=term))
            q_objects.append(Q(mobile_number__icontains=term))
            q_objects.append(Q(home_number__icontains=term))
            q_objects.append(Q(parent_number__icontains=term))
            q_objects.append(Q(user__first_name__icontains=term))
            q_objects.append(Q(user__last_name__icontains=term))

        # Start with a bare QuerySet
        return self.filter(reduce(operator.or_, q_objects))


class Student(models.Model):
    """
    Halaqat Student
    """
    dob = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,
                              default='M', verbose_name=_('Gender'))
    civil_id = models.CharField(max_length=12, unique=True,
                                verbose_name=_('Civil ID'))
    mobile_number = models.CharField(max_length=12, verbose_name=_('Mobile'))
    home_number = models.CharField(max_length=12, verbose_name=_('Home'))
    parent_number = models.CharField(max_length=12, verbose_name=_('Parents'))
    grade = models.CharField(max_length=5, verbose_name=_('Grade'), blank=True)
    school = models.CharField(
        max_length=12, verbose_name=_('School'), blank=True)
    nationality = models.ForeignKey(Nationality, verbose_name=_('Nationality'),
                                    null=True, blank=True)
    address = models.CharField(max_length=150, verbose_name=_('Address'),
                               blank=True)
    parent_email = models.EmailField(
        verbose_name=_('Parent Email'), blank=True)
    halaqat_class = models.ForeignKey(to=HalaqatClass, null=True, blank=True,
                                      verbose_name=_("Halaqat"))
    enrollment_date = models.DateField(verbose_name=_('Enrollment Date'),
                                       null=True)
    old_enrollment_date = models.DateField(null=True,
                                           verbose_name=_('Previous Center Enrollment Date'))
    chapter_memorized = models.IntegerField(default=0,
                                            verbose_name=_('Chapters Memorized'))
    chapter_memorized_with_center = models.IntegerField(default=0,
                                                        verbose_name=_('Chapters memorized with center'))
    status = models.CharField(max_length=1, choices=STATUS_CHOICES,
                              default=PENDING,
                              verbose_name=_('Status'))
    user = models.ForeignKey(User, related_name='student_profile')
    objects = StudnetManager()

    def activate(self):
        self.status = ACTIVE
        self.save()

    def suspend(self):
        self.status = SUSPENDED
        self.save()

    def on_leave(self):
        self.status = ON_LEAVE
        self.save()

    def get_absolute_url(self):
        return reverse('student-detail', args=(self.pk,))
