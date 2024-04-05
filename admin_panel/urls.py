from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.admin_login, name='admin_login'),
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('manage-students/', views.manage_students, name='manage_students'),
    path('create-students/', views.create_student, name='create_students'),
    path('view-students/', views.view_students, name='view_students'),
]
