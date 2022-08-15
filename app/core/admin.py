from django.contrib import admin
from django.contrib.admin import ModelAdmin as BaseUserAdmin
from core import models


class CustomUserAdmin(BaseUserAdmin):
    """Define admin pages for list of users"""
    ordering = ['id']
    list_display = ['pk', 'email']


admin.site.register(models.User, CustomUserAdmin)
