from django.contrib.auth.models import User
from django.db import models
import random
import string

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=4)
    password = models.CharField(max_length=3)

    @staticmethod
    def generate_username():
        return ''.join(random.choices(string.digits, k=4))

    @staticmethod
    def generate_password():
        return ''.join(random.choices(string.ascii_lowercase, k=3))

    @classmethod
    def create_student(cls):
        user = User.objects.create_user(username=cls.generate_username(),
                                        password=cls.generate_password())
        return cls.objects.create(user=user, username=user.username, password=user.password)


