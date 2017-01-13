from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import ugettext as _
from django.views import generic

from back_office.forms import UserChangeForm, UserCreationForm

from braces.views import LoginRequiredMixin, StaffuserRequiredMixin

from .forms import StudentChangeForm, StudentForm
from .models import Student


class StudentListView(LoginRequiredMixin,
                      StaffuserRequiredMixin,
                      generic.ListView):
    model = Student
    context_object_name = 'students'
    template_name = 'students/student_list.html'
    allow_empty = True
    paginate_by = 25

    def get_queryset(self):
        result = super(StudentListView, self).get_queryset()
        search_query = self.request.GET.get('q', None)
        if search_query:
            result = Student.objects.search(search_query)
        return result


class StudentCreationView(LoginRequiredMixin,
                          StaffuserRequiredMixin,
                          SuccessMessageMixin,
                          generic.CreateView):
    template_name = 'students/student_form.html'
    form_class = StudentForm
    model = Student
    second_form_class = UserCreationForm
    success_message = _('Student profile saved successfully')

    def get_context_data(self, **kwargs):
        context = super(StudentCreationView, self).get_context_data(**kwargs)
        context['user_form'] = self.second_form_class
        return context

    def form_valid(self, form):
        user_form = UserCreationForm(self.request.POST)
        if user_form.is_valid():
            user = user_form.save()
            student = form.save(commit=False)
            student.user = user
            student.save()

        return super(StudentCreationView, self).form_valid(form)

    def form_invalid(self, form):
        user_form = UserCreationForm(self.request.POST)
        return self.render_to_response({'form': form,
                                        'user_form': user_form})


class StudentChangeView(LoginRequiredMixin,
                        StaffuserRequiredMixin,
                        SuccessMessageMixin,
                        generic.UpdateView):
    template_name = 'students/student_form.html'
    form_class = StudentChangeForm
    model = Student
    second_form_class = UserChangeForm
    success_message = _('Student profile saved successfully')

    def get_context_data(self, **kwargs):
        context = super(StudentChangeView, self).get_context_data(**kwargs)
        context['user_form'] = self.second_form_class(self.request.POST or None,
                                                      instance=self.object.user)

        return context

    def form_valid(self, form):
        user_form = UserChangeForm(self.request.POST,
                                   instance=self.object.user)
        if user_form.is_valid():
            user_form.save()
        return super(StudentChangeView, self).form_valid(form)
