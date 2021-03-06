from django.db import models
from django.utils.translation import ugettext_lazy as _

GENDER_CHOICES = (
    (u'M', _(u'Male')),
    (u'F', _(u'Female')),
)


class Nationality(models.Model):
    """
    Nationality
    """
    name = models.CharField(max_length=10, verbose_name=_('Name'), unique=True)
    is_active = models.BooleanField(default=True, verbose_name=_('Active'))

    class Meta:
        verbose_name = _('Nationality')
        verbose_name_plural = _('Nationalities')
