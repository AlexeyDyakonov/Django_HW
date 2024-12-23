from django.db import models
from django.contrib.auth.models import AbstractUser

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    username = None
    email = models.EmailField(
        verbose_name="почта",
        unique=True
    )
    avatar = models.ImageField(
        upload_to="users/avatars/",
        **NULLABLE,
        verbose_name="Аватар",
        help_text="Загрузите фото",
    )
    phone = models.CharField(
        max_length=35,
        verbose_name="Телефон",
        **NULLABLE,
        help_text="Введите номер телефона",
    )
    country = models.CharField(
        max_length=50,
        verbose_name="Страна",
        help_text="Введите страну"
    )
    token = models.CharField(
        max_length=100,
        verbose_name="Токен",
        **NULLABLE,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
