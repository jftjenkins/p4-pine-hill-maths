from django.urls import path
from .views import student_login, get_all_lesson, get_question_page


urlpatterns = [
    path("login/", student_login, name="student_login"),  # Student login page
    path("lessons/", get_all_lesson, name="lessons"),  # Page listing maths lessons
    path(
        "question/<str:question_type>/<str:difficulty>/",
        get_question_page,
        name="question_page",
    ),  # Question page,
]
