from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.contrib.auth.models import User


class UserAdmin(DjangoUserAdmin):
    filter_horizontal = ("user_permissions",)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
