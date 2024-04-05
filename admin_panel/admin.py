from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Teacher
from .forms import TeacherCreationForm

class TeacherAdmin(UserAdmin):
    add_form = TeacherCreationForm
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
    )
    search_fields = ('username',)
    ordering = ('username',)

# Register the Teacher model with the custom admin class
admin.site.register(Teacher, TeacherAdmin)
