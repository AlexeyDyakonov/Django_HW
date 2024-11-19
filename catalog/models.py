from decimal import Decimal

from django.db import models

from users.models import User

NULLABLE = {"blank": True, "null": True}


class Category(models.Model):
    name_category = models.CharField(
        max_length=100, verbose_name="Наименование категории"
    )
    description_category = models.TextField(
        verbose_name="Описание категории", **NULLABLE
    )

    def __str__(self):
        return self.name_category

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание товара")
    image = models.ImageField(
        upload_to="products/photo", verbose_name="Изображение товара", **NULLABLE
    )
    category = models.ForeignKey(
        to=Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория товара",
        **NULLABLE,
        related_name="products"
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=Decimal("0.00"),
        verbose_name="Цена за за покупку",
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="дата создания")
    updated_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата последнего изменения",
    )
    view_counter = models.PositiveIntegerField(
        verbose_name="Счетчик просмотров",
        help_text="Укажите количество просмотров",
        default=0
    )
    is_published = models.BooleanField(
        default=True,
        verbose_name='Опубликовано'
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        verbose_name="Владелец",
        help_text="Укажите владельца",
        **NULLABLE,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ["name"]
        permissions = [("set_published", "Can publish product"),
                       ("change_description", "Can change description"),
                       ("change_category", "Can change category")
    ]


class Version(models.Model):
    product = models.ForeignKey(
        Product,
        related_name="product",
        on_delete=models.SET_NULL,
        **NULLABLE,
        verbose_name="продукт",
    )
    version_number = models.CharField(
        max_length=200, verbose_name="Номер версии", help_text="Введите номер версии"
    )
    version_name = models.CharField(
        max_length=200,
        verbose_name="Название версии",
        help_text="Введите название версии",
    )
    sign = models.BooleanField(
        verbose_name="Признак текущей версии"
    )

    def __str__(self):
        return self.version_name

    class Meta:
        verbose_name = "версия"
        verbose_name_plural = "версии"
        ordering = ["product", "version_number", "version_name", "sign"]
