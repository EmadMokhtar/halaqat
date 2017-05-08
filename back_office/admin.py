from django.contrib import admin

from .models import ClassType, HalaqatClass, Teacher

admin.site.register(Teacher)
admin.site.register(ClassType)
admin.site.register(HalaqatClass)
