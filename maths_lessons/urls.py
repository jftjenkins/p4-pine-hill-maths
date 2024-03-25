from django.urls import path
from . import views

urlpatterns = [
    # URL pattern for the maths lessons view
    path('lessons/', views.maths_lessons_view, name='maths_lessons'),
]