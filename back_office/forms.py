from crispy_forms.helper import FormHelper
from crispy_forms.layout import HTML, Div, Layout
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _, ugettext

from .models import DAYS_CHOICES, ClassType, HalaqatClass, Teacher


class UserCreationForm(forms.ModelForm):
    """
    New user form
    """
    helper = FormHelper()
    helper.form_tag = False
    helper.layout = Layout(
        Div(
            Div(
                HTML(_('<h3 class="panel-title">User Info</h3>')),
                css_class='panel-heading',
            ),
            Div(
                Div(
                    Div('first_name', css_class='col-md-6'),
                    Div('last_name', css_class='col-md-6'),
                    css_class='row'
                ),
                Div(
                    Div('username', css_class='col-md-6'),
                    Div('email', css_class='col-md-6'),
                    css_class='row'),
                Div(
                    Div('password1', css_class='col-md-6'),
                    Div('password2', css_class='col-md-6'),
                    css_class='row'
                ),
                css_class='panel-body'),
            css_class='panel panel-default',
        ),
    )

    password1 = forms.CharField(widget=forms.PasswordInput,
                                label=_('Password'))
    password2 = forms.CharField(widget=forms.PasswordInput,
                                label=_('Password confirmation'))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'username']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2


class UserChangeForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'readonly': 'readonly'},),
        label=_('Username')
    )
    helper = FormHelper()
    helper.form_tag = False
    helper.layout = Layout(
        Div(
            Div(
                HTML(_('<h3 class="panel-title">User Info</h3>')),
                css_class='panel-heading',
            ),
            Div(
                Div(
                    Div('first_name', css_class='col-md-6'),
                    Div('last_name', css_class='col-md-6'),
                    css_class='row'
                ),
                Div(
                    Div('username', css_class='col-md-6'),
                    Div('email', css_class='col-md-6'),
                    css_class='row'),
                css_class='panel-body'),
            css_class='panel panel-default',
        ),
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username')

    def clean_password(self):
        return self.initial['password']


class TeacherForm(forms.ModelForm):
    """
    Form for teacher model
    """
    helper = FormHelper()
    helper.form_tag = False
    helper.layout = Layout(
        Div(
            Div(
                HTML(_('<h3 class="panel-title">Teacher Info</h3>')),
                css_class='panel-heading',
            ),
            Div(
                Div(
                    Div('civil_id', css_class='col-md-6'),
                    Div('gender', css_class='col-md-6'),
                    css_class='row'
                ),
                Div(
                    Div('phone_number', css_class='col-md-6'),
                    Div('job_title', css_class='col-md-6'),
                    css_class='row'), css_class='panel-body'),
            css_class='panel panel-default',
        ),
    )

    class Meta:
        model = Teacher
        fields = ['gender', 'civil_id', 'phone_number', 'job_title']


class ClassTypeForm(forms.ModelForm):
    """
    Form for haqalat Class Type
    """

    class Meta:
        model = ClassType
        fields = ['name', 'monthly_fees']


class ClassForm(forms.ModelForm):
    """
    Form for halaqat class
    """

    days = forms.MultipleChoiceField(choices=DAYS_CHOICES,
                                     widget=forms.CheckboxSelectMultiple(),
                                     localize=True,
                                     label=_("Days"))
    first_semester_start = forms.DateField(localize=True,
                                           input_formats=['%d/%m/%Y'],
                                           label=_('First Semester Start'))
    first_semester_end = forms.DateField(localize=True,
                                         input_formats=['%d/%m/%Y'],
                                         label=_('First Semester End'))
    second_semester_start = forms.DateField(localize=True,
                                            input_formats=['%d/%m/%Y'],
                                            label=_('Second Semester Start'))
    second_semester_end = forms.DateField(localize=True,
                                          input_formats=['%d/%m/%Y'],
                                          label=_('Second Semester End'))
    start_time = forms.TimeField(localize=True,
                                 input_formats=['%I:%M %p'],
                                 label=_('Start Time'))
    end_time = forms.TimeField(localize=True,
                               input_formats=['%I:%M %p'],
                               label=_('End Time'))

    class Meta:
        model = HalaqatClass
        fields = ['name', 'class_type', 'gender', 'teacher', 'days',
                  'start_time', 'end_time', 'first_semester_start',
                  'first_semester_end', 'second_semester_start',
                  'second_semester_end']
