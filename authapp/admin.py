from django.contrib import admin
from .models import User

# Register your models here.
admin.site.site_header = "Cuadros Marcel"


class AdminUser(admin.ModelAdmin):
    list_display = ("get_first_name", "get_last_name", "email", "phone", "address", "is_staff")


admin.site.register(User, AdminUser)
