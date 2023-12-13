
from django import forms
from .models import Students, Grade


class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ['Name', 'Roll', 'City', 'Grade']


class GradeForm(forms.Form):
    class Meta:
        model = Grade
        fields = ['Grade']
