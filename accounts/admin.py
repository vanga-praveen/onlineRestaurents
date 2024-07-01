from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class CustomUserAdmin(UserAdmin):
    # list_display = ('first_name', 'last_name', 'username', 'email', 'role', 'is_active')
    # ordering = ('-first_name',)

    filter_horizantal = ()
    list_filter = ()
    fieldsets = ()



admin.site.register(User, CustomUserAdmin)