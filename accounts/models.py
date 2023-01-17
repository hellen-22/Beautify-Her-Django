from django.db import models
from django.contrib import admin
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    bio = models.TextField()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username', 'bio']

    def __str__(self):
        return self.username

class CustomerProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name

    @admin.display(ordering='user__first_name')
    def firstname(self):
        return self.user.first_name

    @admin.display(ordering='user__bio')
    def bio(self):
        return self.user.bio

class ServiceProviderProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)

    def __str__(self):
        return self.user.first_name

    @admin.display(ordering='user__username')
    def username(self):
        return self.user.username
