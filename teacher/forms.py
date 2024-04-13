from django import forms
from .models import Teacher

class TeacherCreationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = Teacher
        fields = ('username', 'password', 'is_staff')  # Add 'is_staff' to fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['is_staff'].initial = True  # Set 'is_staff' to True by default
