# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.forms import ModelForm, CharField, EmailField, ValidationError


class StudentForm(ModelForm):
    username = CharField(label='username', max_length=150)
    email = EmailField(label='Email address')

    class Meta:
        model = User
        fields = ['username', 'password', 'email']  # Assuming Student model has these fields

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("This email address is already in use.")
        return email
