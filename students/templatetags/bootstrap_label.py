from django import template
from django.utils.safestring import mark_safe

lable_type = {'Pending': 'default',
              'Active': 'success',
              'Suspended': 'danger',
              'On Leave': 'warning',
              'غير ملتحق': 'default',
              'ملتحق': 'success',
              'موقوف': 'danger',
              'في أجازة': 'warning',
              }

register = template.Library()


@register.filter
def student_status_label(status):
    status_label_type = lable_type.get(status)
    lable = '<span class="label label-{}">{}</span>'.format(status_label_type,
                                                            status)
    return mark_safe(lable)
