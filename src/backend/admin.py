from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import UserProfileCreationForm, UserProfileChangeForm
from .models import UserProfile, BookAdd, Bookinfo, BookAuthor, BookCategory, BookCode, BookPublication


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


class BookInfoAdmin(admin.ModelAdmin):
    list_display = ('Book_Name', 'Book_Author', 'Book_Ifsc',
                    'Book_Category', 'Availability_Status')
    search_fields = ('Book_Name', 'Book_Author', 'Book_Ifsc',
                     'Book_Category', 'Availability_Status')
    list_filter = ('Book_Name', 'Book_Author', 'Book_Ifsc',
                   'Book_Category', 'Availability_Status')


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(BookAdd)
admin.site.register(Bookinfo, BookInfoAdmin)
admin.site.register(BookAuthor)
admin.site.register(BookCategory)
admin.site.register(BookCode)
admin.site.register(BookPublication)
