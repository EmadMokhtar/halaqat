from django import forms
from django.contrib.auth.models import User
from .models import Teacher


class UserCreationForm(forms.ModelForm):
    """
    New user form
    """
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

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
    username = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username')

    def clean_password(self):
        return self.initial['password']


class TeacherForm(forms.ModelForm):
    """
    Form for teacher model
    """

    class Meta:
        model = Teacher
        fields = ['gender', 'civil_id', 'phone_number', 'job_title']
