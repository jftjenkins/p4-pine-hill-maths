from django.db import models
from django.contrib.auth.models import User
import random
import string

class AdminLogin(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.action} - {self.timestamp}"

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=4)
    password = models.CharField(max_length=3)

    @staticmethod
    def generate_unique_username():
        while True:
            username = ''.join(random.choices(string.digits, k=4))
            if not Student.objects.filter(username=username).exists():
                return username

    @staticmethod
    def generate_unique_password():
        while True:
            password = ''.join(random.choices(string.ascii_lowercase, k=3))
            if not Student.objects.filter(password=password).exists():
                return password

    @classmethod
    def create_student(cls):
        username = cls.generate_unique_username()
        password = cls.generate_unique_password()
        user = User.objects.create_user(username=username, password=password)
        return cls.objects.create(user=user, username=username, password=password)

