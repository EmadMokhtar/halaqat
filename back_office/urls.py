from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^teacher/new/$', views.TeacherCreation.as_view(), name='teacher_creation'),
    url(r'^teacher/$', views.TeacherList.as_view(), name='teacher_list'),
    url(r'^teacher/details/(?P<pk>\d+)$', views.TeacherUpdate.as_view(), name='teacher_details'),
]