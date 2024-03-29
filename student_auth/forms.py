from django import forms

class StudentSignInForm(forms.Form):
    username = forms.CharField(label='Username', max_length=4)
    password = forms.CharField(label='Password', max_length=3, widget=forms.PasswordInput)
