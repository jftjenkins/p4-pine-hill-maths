from django.urls import path
from .views import IndexView, MathsLessonsView

urlpatterns = [
    path('', IndexView.as_view(), name='home'),  # Home URL pattern
    path('lessons/', MathsLessonsView.as_view(), name='maths_lessons'),  # Maths lessons URL pattern
]

