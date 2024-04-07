from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.student_login, name='student_login'),  # Student login page
    path('lessons/', views.lessons, name='lessons'),  # Page listing maths lessons
    path('question/<str:type>/<str:difficulty>/', views.question_page, name='question_page'),  # Question page
]
