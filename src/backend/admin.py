from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from .forms import UserProfileCreationForm, UserProfileChangeForm
from .models import UserProfile
# Register your models here.


class UserProfileAdmin(UserAdmin):
    add_form = UserProfileCreationForm
    form = UserProfileChangeForm
    list_display = ['Email', 'Full_Name', 'Mob_Number', 'admin', 'is_staff']
    fieldsets = (
        (None, {'fields': ('Email',  'password')}),
        ('Personal Info', {
            'fields': ('Full_Name', 'Mob_Number', 'ProfilePhoto')}),
        ('Permissions', {'fields': ('date_joined', 'is_staff',
         'is_active', 'admin')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('Email',  'password1', 'password2', 'is_staff', 'is_active', 'admin')}
         ),
    )
    search_fields = ['Email', 'Mob_Number', 'Full_Name']
    ordering = ['Email', 'Mob_Number']


admin.site.register(UserProfile, UserProfileAdmin)
