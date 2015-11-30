from django.forms import ModelForm
from .models import Teacher


class TeacherForm(ModelForm):
    """
    Form for teacher model
    """

    class Meta:
        model = Teacher
        fields = ['name', 'gender', 'civil_id', 'phone_number', 'job_title']