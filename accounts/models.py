from django.db import models
from django.contrib import admin
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    bio = models.TextField()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username']

    def __str__(self) -> str:
        return self.username


class ServiceProviderProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.user.first_name

    @admin.display(ordering='user__username')
    def username(self):
        return self.user.username
