"""
URL configuration for pine_hills_maths project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from maths_lessons.views import IndexView, MathsLessonsView, AdminLoginView
from student_auth.views import student_authenticate

urlpatterns = [
    path('', IndexView.as_view(), name='home'),  # Home URL pattern
    path('lessons/', MathsLessonsView.as_view(template_name="lessons.html"), name='maths_lessons'),  # Maths lessons URL pattern
    path('student/login/', TemplateView.as_view(template_name="signin.html"), name='student_login'),  # Student login page
    path('student/authenticate/', student_authenticate, name='student_authenticate'),  # Student authentication URL pattern
    path('about/', TemplateView.as_view(template_name="about.html"), name="about"),  # About page
    path('teacher/', include('admin_panel.urls')),  # Include admin_panel URLs
    path('admin/', admin.site.urls),  # Django admin site
]