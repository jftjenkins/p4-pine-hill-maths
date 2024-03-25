from django.contrib.auth.models import User
from django.db import models

# Model for representing maths lessons
class MathsLesson(models.Model):
    DIFFICULTY_CHOICES = [
        ('level_1', 'Level 1'),
        ('level_2', 'Level 2'),
        ('level_3', 'Level 3'),
    ]

    TYPE_CHOICES = [
        ('addition', 'Addition'),
        ('subtraction', 'Subtraction'),
        ('multiplication', 'Multiplication'),
        ('division', 'Division'),
    ]

    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES)
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.get_difficulty_display()} {self.get_type_display()} Lesson"


# Model for representing student progress in maths lessons
class StudentProgress(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(MathsLesson, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student.username}'s Progress: {self.lesson}"
