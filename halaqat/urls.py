from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.contrib.auth import views as auth_views

from back_office import urls as back_office_url
from students import urls as students_url
from .views import IndexView

urlpatterns = i18n_patterns(
    url(r'^$', view=IndexView.as_view(), name='home'),
    url(r'^login/$', auth_views.login,
        {'template_name': 'login.html'},
        name='login'),
    url(r'^logout/$', auth_views.logout,
        {'next_page': '/login'}, name='logout'),
    url(r'^back-office/', include(back_office_url)),
    url(r'^back-office/students/', include(students_url)),
    url(r'^admin/', include(admin.site.urls)),
)
