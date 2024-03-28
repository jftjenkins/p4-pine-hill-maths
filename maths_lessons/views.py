from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView

class IndexView(TemplateView):
    template_name = 'home.html'

class MathsLessonsView(TemplateView):
    template_name = 'lessons.html'

class AdminLoginView(LoginView):
    template_name = 'admin_login.html'
