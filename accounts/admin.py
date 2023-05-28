from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import *
# Register your models here.
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('username', 'first_name', 'last_name', 'bio')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'role')}),
    )
    add_fieldsets = (
        (None, {'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}),
    )


@admin.register(Customer)
class CustomerProfile(admin.ModelAdmin):
    list_display = ['firstname', 'bio']

@admin.register(ServiceProvider)
class ProviderProfileAdmin(admin.ModelAdmin):
    list_display = ['username', 'location', 'phone_number']
