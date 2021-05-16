from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


# Register your models here.
User = get_user_model()


class UserAdmin(BaseUserAdmin):
    list_display = ['Email', 'Full_Name', 'Mob_Number', 'admin']
    list_filter = ['admin']
    fieldsets = (
        (None, {'fields': ('Email', 'password')}),
        ('Personal Info', {
         'fields': ('Full_Name', 'Mob_Number', 'ProfilePhoto')}),
        ('Permissions', {'fields': ('admin', 'is_staff', 'is_active')}),
    )

    search_fields = ['Email', 'Mob_Number', 'Full_Name']
    ordering = ['Email', 'Mob_Number']
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
