from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
# Register your models here.

class CustomUserAdmin(UserAdmin):
    list_display = ['username','email','is_active','is_staff','is_superuser','last_name',"first_name"]
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email","username", "password1", "password2"),
            },
        ),
    )
admin.site.register(CustomUser, CustomUserAdmin)

