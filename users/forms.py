from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm, UserChangeForm
from catalog.forms import StyleFormMixin
from users.models import User


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    """
    Форма регистрации
    """
    class Meta:
        model = User
        fields = ("email",
                  "password1",
                  "password2"
        )


class UserPasswordResetForm(StyleFormMixin, PasswordResetForm):
    """
    Форма сброса пароля
    """
    class Meta:
        model = User
        fields = ("email")
