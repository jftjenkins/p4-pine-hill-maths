from django.contrib.auth.models import User
from django.db import models

class UserLogin(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"User login by {self.user.username} at {self.timestamp}"

