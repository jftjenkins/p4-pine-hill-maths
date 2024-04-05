from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('login/', TemplateView.as_view(template_name="signin.html"), name='student_login'),  # Student login page
]