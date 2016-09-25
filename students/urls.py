from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',
        view=views.StudentList.as_view(),
        name='student-list'),
    url(r'^new/$',
        view=views.StudentCreation.as_view(),
        name='student-new'),
    url(r'^(?P<pk>\d+)/',
        view=views.StudentChangeView.as_view(),
        name='student-detail'),
]
