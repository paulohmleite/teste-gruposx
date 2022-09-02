from django.contrib import admin

from contas.models import User

from .forms import UserChangeForm, UserCreationForm
from django.contrib.auth.admin import UserAdmin


class UserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = [
        "username",
    ]


admin.site.register(User, UserAdmin)
