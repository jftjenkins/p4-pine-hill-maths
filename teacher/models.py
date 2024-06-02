from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm, CharField, EmailField, ValidationError

class StudentForm(ModelForm):
    username = CharField(label='Username', max_length=150)
    email = EmailField(label='Email address')
    password = CharField(label='Password', required=False, widget=forms.PasswordInput, help_text='Leave blank to keep the current password.')

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def __init__(self, *args, **kwargs):
        self.instance = kwargs.get('instance')
        super().__init__(*args, **kwargs)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exclude(id=self.instance.id).exists():
            raise ValidationError("This email address is already in use.")
        return email
