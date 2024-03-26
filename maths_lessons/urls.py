from django.urls import path
from .views import IndexView, MathsLessonsView

urlpatterns = [
    # URL pattern for the index view
    path('', IndexView.as_view(), name='home'),
    # URL pattern for the maths lessons view
    path('lessons/', MathsLessonsView.as_view(), name='maths_lessons'),
]
