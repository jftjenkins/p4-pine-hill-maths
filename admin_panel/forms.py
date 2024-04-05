from django import forms
from .models import Teacher

class TeacherCreationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = Teacher
        fields = ('username', 'password')
