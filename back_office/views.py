from braces.views import LoginRequiredMixin, StaffuserRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.utils.translation import ugettext_lazy as _
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView

from .forms import (ClassForm, ClassTypeForm, TeacherForm, UserChangeForm,
                    UserCreationForm)
from .models import ClassType, HalaqatClass, Teacher


class TeacherList(LoginRequiredMixin,
                  StaffuserRequiredMixin,
                  ListView):
    """
    Show list of teachers in center
    """
    model = Teacher
    template_name = 'back_office/teacher_list.html'
    context_object_name = 'teachers'
    allow_empty = True


class TeacherCreation(LoginRequiredMixin,
                      StaffuserRequiredMixin,
                      SuccessMessageMixin,
                      CreateView):
    """
    Creates new teacher
    """
    template_name = "back_office/teacher_form.html"
    form_class = TeacherForm
    model = Teacher
    second_form_class = UserCreationForm
    success_message = _("Teacher profile created successfully")

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


class TeacherUpdate(LoginRequiredMixin,
                    StaffuserRequiredMixin,
                    SuccessMessageMixin,
                    UpdateView):
    """
    Update teacher profile
    """
    model = Teacher
    template_name = 'back_office/teacher_form.html'
    form_class = TeacherForm
    second_form_class = UserChangeForm
    success_message = _("Teacher profile updated successfully")

    def get_context_data(self, **kwargs):
        context = super(TeacherUpdate, self).get_context_data(**kwargs)
        context['user_form'] = self.second_form_class(self.request.POST or None,
                                                      instance=self.object.user)

        return context

    def form_valid(self, form):
        user_form = UserChangeForm(
            self.request.POST, instance=self.object.user)
        if user_form.is_valid():
            user_form.save()
        return super(TeacherUpdate, self).form_valid(form)


class ClassTypeList(LoginRequiredMixin,
                    StaffuserRequiredMixin,
                    ListView):
    """
    Halaqat class type list view
    """
    model = ClassType
    template_name = 'back_office/class_type_list.html'
    context_object_name = 'class_types'
    allow_empty = True


class ClassTypeCreation(LoginRequiredMixin,
                        StaffuserRequiredMixin,
                        SuccessMessageMixin,
                        CreateView):
    """
    Create halaqat class type view
    """
    model = ClassType
    form_class = ClassTypeForm
    template_name = 'back_office/class_type_form.html'
    success_message = _("Class Type created successfully")


class ClassTypeUpdate(LoginRequiredMixin,
                      StaffuserRequiredMixin,
                      SuccessMessageMixin,
                      UpdateView):
    """
    Update halaqat class type view
    """
    model = ClassType
    form_class = ClassTypeForm
    template_name = 'back_office/class_type_form.html'
    success_message = _("Class Type updated successfully")


class ClassList(LoginRequiredMixin,
                StaffuserRequiredMixin,
                ListView):
    """
    List of class in halaqat
    """
    model = HalaqatClass
    template_name = 'back_office/class_list.html'
    context_object_name = 'classes'
    allow_empty = True


class ClassCreation(LoginRequiredMixin,
                    StaffuserRequiredMixin,
                    SuccessMessageMixin,
                    CreateView):
    """
    Create halaqat class view
    """
    model = HalaqatClass
    form_class = ClassForm
    template_name = 'back_office/class_form.html'
    success_message = _("Class created successfully")


class ClassUpdate(LoginRequiredMixin,
                  StaffuserRequiredMixin,
                  SuccessMessageMixin,
                  UpdateView):
    """
    Update halaqat class view
    """
    model = HalaqatClass
    form_class = ClassForm
    template_name = 'back_office/class_form.html'
    success_message = _("Class updated successfully")
