from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import *
# Register your models here.
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    pass

@admin.register(CustomerProfile)
class CustomerProfile(admin.ModelAdmin):
    list_display = ['firstname', 'bio']

@admin.register(ServiceProviderProfile)
class ProviderProfileAdmin(admin.ModelAdmin):
    list_display = ['username', 'location', 'phone_number']
