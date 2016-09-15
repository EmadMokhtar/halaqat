from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.db import transaction

from .models import Student
from .forms import StudentForm

from back_office.forms import UserCreationForm


class StudentList(generic.ListView):
    model = Student
    context_object_name = 'students'
    template_name = 'students/student_list.html'
    allow_empty = True


class StudentCreation(SuccessMessageMixin, generic.CreateView):
    template_name = 'students/student_form.html'
    form_class = StudentForm
    model = Student
    second_from_class = UserCreationForm
    success_message = 'Student profile saved successfully'

    def get_context_data(self, **kwargs):
        context = super(StudentCreation, self).get_context_data(**kwargs)
        context['user_form'] = self.second_from_class
        return context

    def form_valid(self, form):
        user_form = UserCreationForm(self.request.POST)
        if not user_form.is_valid():
            return self.render_to_response({'form': form,
                                            'user_form': user_form})
        try:
            with transaction.atomic():
                user = user_form.save()
                student = form.save(commit=False)
                student.user = user
                student.save()
                return HttpResponseRedirect(self.get_success_url())
        except Exception:
             return self.render_to_response({'form': form,
                                             'user_form': user_form})

    def form_invalid(self, form):
        user_form = UserCreationForm(self.request.POST)
        return self.render_to_response({'form': form,
                                        'user_form': user_form})
