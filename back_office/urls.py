from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^teacher/$', views.TeacherList.as_view(), name='teacher-list'),
    url(r'^teacher/new/$', views.TeacherCreation.as_view(), name='teacher-new'),
    url(r'^teacher/(?P<pk>\d+)$', views.TeacherUpdate.as_view(), name='teacher-detail'),
    url(r'^class-type/$', views.ClassTypeList.as_view(), name='class_type-list'),
    url(r'^class-type/new/$', views.ClassTypeCreation.as_view(), name='class_type-new'),
    url(r'^class-type/(?P<pk>\d+)$', views.ClassTypeUpdate.as_view(), name='class_type-detail'),
    url(r'^class/$', views.ClassList.as_view(), name='class-list'),
    url(r'^class/new/$', views.ClassCreation.as_view(), name='class-new'),
    url(r'^class/(?P<pk>\d+)$', views.ClassUpdate.as_view(), name='class-details'),
]
