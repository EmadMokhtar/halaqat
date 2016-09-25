from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, HTML
from django import forms

from students.models import Student


class StudentForm(forms.ModelForm):
    dob = forms.DateField(widget=forms.DateInput(
                          attrs={'class': 'datepicker'})
                          )
    address = forms.CharField(widget=forms.Textarea())
    helper = FormHelper()
    helper.form_tag = False
    helper.layout = Layout(
        Div(
            Div(
                HTML('<h3 class="panel-title">Basic Info</h3>'),
                css_class='panel-heading',
            ),
            Div(
                Div(
                    Div('civil_id', css_class='col-md-6'),
                    Div('dob', css_class='col-md-6')
                    , css_class='row'
                ),
                Div(
                    Div('gender', css_class='col-md-6'),
                    Div('nationality', css_class='col-md-6')
                    , css_class='row'
                ),
                Div(
                    Div('school', css_class='col-md-6'),
                    Div('grade', css_class='col-md-6')
                    , css_class='row'
                )
                , css_class='panel-body'),  # Fields
            css_class='panel panel-default', ),
        Div(
            Div(
                HTML('<h3 class="panel-title">Contact Info</h3>'),
                css_class='panel-heading',
            ),
            Div(
                Div(
                    Div('mobile_number', css_class='col-md-6'),
                    Div('home_number', css_class='col-md-6')
                    , css_class='row'),
                Div(
                    Div('parent_number', css_class='col-md-6'),
                    Div('parent_email', css_class='col-md-6')
                    , css_class='row'),
                Div(
                    Div('address', css_class='col-md-12')
                    , css_class='row')
                , css_class='panel-body'),  # Fields
            css_class='panel panel-default', ),
        Div(
            Div(
                HTML('<h3 class="panel-title">Halaqat Info</h3>'),
                css_class='panel-heading',
            ),
            Div(
                Div(
                    Div('halaqat_class', css_class='col-md-6'),
                    Div('status', css_class='col-md-6')
                    , css_class='row'),
                Div(
                    Div('chapter_memorized', css_class='col-md-6'),
                    Div('chapter_memorized_with_center', css_class='col-md-6')
                    , css_class='row'
                    )
                , css_class='panel-body'),  # Fields
            css_class='panel panel-default',
            ),
    )

    class Meta:
        model = Student
        fields = ('dob', 'gender', 'civil_id', 'mobile_number', 'home_number',
                  'parent_number', 'grade', 'school', 'nationality', 'address',
                  'parent_email', 'halaqat_class', 'chapter_memorized',
                  'chapter_memorized_with_center', 'status')


class StudentChangeForm(forms.ModelForm):
    dob = forms.DateField(widget=forms.DateInput(
                          attrs={'class': 'datepicker'})
                          )
    address = forms.CharField(widget=forms.Textarea())
    helper = FormHelper()
    helper.form_tag = False
    helper.layout = Layout(
        Div(
            Div(
                HTML('<h3 class="panel-title">Basic Info</h3>'),
                css_class='panel-heading',
            ),
            Div(
                Div(
                    Div('civil_id', css_class='col-md-6'),
                    Div('dob', css_class='col-md-6')
                    , css_class='row'
                ),
                Div(
                    Div('gender', css_class='col-md-6'),
                    Div('nationality', css_class='col-md-6')
                    , css_class='row'
                ),
                Div(
                    Div('school', css_class='col-md-6'),
                    Div('grade', css_class='col-md-6')
                    , css_class='row'
                )
                , css_class='panel-body'),  # Fields
            css_class='panel panel-default', ),
        Div(
            Div(
                HTML('<h3 class="panel-title">Contact Info</h3>'),
                css_class='panel-heading',
            ),
            Div(
                Div(
                    Div('mobile_number', css_class='col-md-6'),
                    Div('home_number', css_class='col-md-6')
                    , css_class='row'),
                Div(
                    Div('parent_number', css_class='col-md-6'),
                    Div('parent_email', css_class='col-md-6')
                    , css_class='row'),
                Div(
                    Div('address', css_class='col-md-12')
                    , css_class='row')
                , css_class='panel-body'),  # Fields
            css_class='panel panel-default', ),
        Div(
            Div(
                HTML('<h3 class="panel-title">Halaqat Info</h3>'),
                css_class='panel-heading',
            ),
            Div(
                Div(
                    Div('halaqat_class', css_class='col-md-6'),
                    Div('status', css_class='col-md-6')
                    , css_class='row'),
                Div(
                    Div('chapter_memorized', css_class='col-md-6'),
                    Div('chapter_memorized_with_center', css_class='col-md-6')
                    , css_class='row'
                    )
                , css_class='panel-body'),  # Fields
            css_class='panel panel-default',
            ),
    )

    class Meta:
        model = Student
        fields = ('dob', 'gender', 'civil_id', 'mobile_number', 'home_number',
                  'parent_number', 'grade', 'school', 'nationality', 'address',
                  'parent_email', 'halaqat_class', 'chapter_memorized',
                  'chapter_memorized_with_center', 'status')
