# accounts/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from contas.models import User


class UserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ("username",)


class UserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = User
        fields = ("username",)
