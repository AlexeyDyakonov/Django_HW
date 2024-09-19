from decimal import Decimal

from django.db import models
from django.db.models import IntegerField

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
        upload_to="products/", verbose_name="Изображение товара", **NULLABLE
    )
    category = models.ForeignKey(
        to = Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория товара",
        **NULLABLE,
        related_name= "products"
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

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ["name"]
