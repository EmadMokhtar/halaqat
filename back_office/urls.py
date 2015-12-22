from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^teacher/$', views.TeacherList.as_view(), name='teacher_list'),
    url(r'^teacher/new/$', views.TeacherCreation.as_view(), name='teacher_new'),
    url(r'^teacher/details/(?P<pk>\d+)$', views.TeacherUpdate.as_view(), name='teacher_details'),
    url(r'class-type/$', views.ClassTypeList.as_view(), name='class_type_list'),
    url(r'class-type/new/$', views.ClassTypeCreation.as_view(), name='class_type_new'),
    url(r'class-type/details/(?P<pk>\d+)$', views.ClassTypeUpdate.as_view(), name='class_type_details'),
]