from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns

from back_office import urls as back_office_url
from students import urls as students_url

urlpatterns = i18n_patterns(
    url(r'^back-office/', include(back_office_url)),
    url(r'^back-office/students/', include(students_url)),
    url(r'^admin/', include(admin.site.urls)),
)
