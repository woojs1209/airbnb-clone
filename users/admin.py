from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# admin.site.register(models.User, CustomUserAdmin)
@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """ Custom User Admin  """
    # make blue box
    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile", 
            {
                "fields" : (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost"
                )
            }
        ),
    )