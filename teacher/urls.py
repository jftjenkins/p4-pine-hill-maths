# teacher/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.teacher_login, name="teacher_login"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("create-students/", views.create_student, name="create_students"),
    path("view-students/", views.view_students, name="view_students"),
    path(
        "edit_student/<int:student_id>/",
        views.edit_student,
        name="edit_student",
    ),
    path(
        "delete_student/<int:student_id>/",
        views.delete_student,
        name="delete_student",
    ),
    path("reset_scoreboard/", views.reset_scoreboard, name="reset_scoreboard"),
]
