from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """Custom User admin with additional fields"""
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('middle_name', 'phone')}),
    )
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        ('Additional Info', {'fields': ('middle_name', 'phone')}),
    )
