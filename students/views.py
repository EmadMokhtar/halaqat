from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.
from .models import Student
from .forms import StudentForm

from back_office.forms import UserCreationForm


class StudentList(generic.ListView):
    model = Student
    context_object_name = 'students'
    template_name = 'students/student_list.html'
    allow_empty = True

