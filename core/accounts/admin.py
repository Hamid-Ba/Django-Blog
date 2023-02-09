from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
import accounts.models as models


class CustomUserAdmin(UserAdmin):
    """User Admin"""

    model = models.User
    list_display = ["email", "is_active", "is_verified", "is_staff", "is_superuser"]
    list_filter = ["email", "is_active", "is_verified", "is_staff", "is_superuser"]
    search_fields = ["email"]
    ordering = ["email"]

    fieldsets = (
        (
            "Authentication",
            {
                "fields": ("email", "password"),
            },
        ),
        (
            "Permissions",
            {
                "fields": ("is_active", "is_verified", "is_staff", "is_superuser"),
            },
        ),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "is_active",
                    "is_verified",
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
    )


admin.site.register(models.Profile)
admin.site.register(models.User, CustomUserAdmin)
