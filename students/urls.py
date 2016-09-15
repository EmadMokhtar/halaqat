from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',
        view=views.StudentList.as_view(),
        name='student-list'),
]
