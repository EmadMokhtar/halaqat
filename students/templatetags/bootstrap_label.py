from django import template
from django.utils.translation import ugettext as _
from django.utils.safestring import mark_safe

lable_type = {_('Pending'): 'default',
              _('Active'): 'success',
              _('Suspended'): 'danger',
              _('On Leave'): 'warning'
              }

register = template.Library()


@register.filter
def student_status_label(status):
    status_label_type = lable_type.get(status)
    lable = '<span class="label label-{}">{}</span>'.format(status_label_type,
                                                            status)
    return mark_safe(lable)
