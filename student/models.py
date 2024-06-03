from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User


# Model for representing maths lessons
class MathsLesson(models.Model):
    DIFFICULTY_CHOICES = [
        ("level_1", "Level 1"),
        ("level_2", "Level 2"),
        ("level_3", "Level 3"),
    ]

    TYPE_CHOICES = [
        ("addition", "Addition"),
        ("subtraction", "Subtraction"),
        ("multiplication", "Multiplication"),
        ("division", "Division"),
    ]

    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES)
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.get_difficulty_display()} {self.get_type_display()} Lesson"


# Scorecard of student
class ScoreCard(models.Model):
    username = models.CharField(max_length=100, default="")
    email = models.CharField(max_length=100, default="")

    test_type = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=100)
    total_questions = models.IntegerField()
    score = models.IntegerField()
    percentage_score = models.FloatField()

    def __str__(self):
        return f"{self.username} - {self.email} - {self.test_type} - {self.difficulty} - Score: {self.score}/{self.total_questions}"
