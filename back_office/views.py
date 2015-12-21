# coding=utf-8
from django.contrib.messages import success
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.core.urlresolvers import reverse
from .forms import TeacherForm, UserCreationForm, UserChangeForm, ClassTypeForm
from .models import Teacher, ClassType


class TeacherList(ListView):
    """
    Show list of teachers in center
    """
    model = Teacher
    template_name = 'back_office/teacher_list.html'
    context_object_name = 'teachers'
    allow_empty = True


class TeacherCreation(SuccessMessageMixin, CreateView):
    """
    Creates new teacher
    """
    template_name = 'back_office/teacher_form.html'
    form_class = TeacherForm
    model = Teacher
    second_form_class = UserCreationForm
    success_message = 'Teacher profile saved successfully'

    def get_context_data(self, **kwargs):
        context = super(TeacherCreation, self).get_context_data(**kwargs)

        context['user_form'] = self.second_form_class

        return context

    def form_valid(self, form):
        user_form = UserCreationForm(self.request.POST)
        if user_form.is_valid():
            user = user_form.save()
            teacher = form.save(commit=False)
            teacher.user_id = user.id
            teacher.save()
        return HttpResponseRedirect(self.get_success_url())


class TeacherUpdate(SuccessMessageMixin, UpdateView):
    """
    Update teacher profile
    """
    model = Teacher
    template_name = 'back_office/teacher_form.html'
    form_class = TeacherForm
    second_form_class = UserChangeForm
    success_message = 'Teacher profile saved successfully'

    def get_context_data(self, **kwargs):
        context = super(TeacherUpdate, self).get_context_data(**kwargs)

        context['user_form'] = self.second_form_class(self.request.POST or None, instance=self.object.user)

        return context

    def form_valid(self, form):
        user_form = UserChangeForm(self.request.POST, instance=self.object.user)
        if user_form.is_valid():
            user_form.save()
        return super(TeacherUpdate, self).form_valid(form)


class ClassTypeList(ListView):
    """
    Halaqat class type list view
    """
    model = ClassType
    template_name = 'back_office/class_type_list.html'
    context_object_name = 'class_types'
    allow_empty = True


class ClassTypeCreation(SuccessMessageMixin, CreateView):
    """
    Create halaqat class type view
    """
    model = ClassType
    form_class = ClassTypeForm
    template_name = 'back_office/class_type_form.html'
    success_message = 'Class Type Created Successfully'


class ClassTypeUpdate(SuccessMessageMixin, CreateView):
    """
    Update halaqat class type view
    """
    model = ClassType
    form_class = ClassTypeForm
    template_name = 'back_office/class_type_form.html'
    success_message = 'Class Type Updated Successfully'
