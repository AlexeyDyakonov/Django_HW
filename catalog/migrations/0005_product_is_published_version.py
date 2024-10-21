# Generated by Django 5.1.1 on 2024-10-21 10:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0004_product_view_counter"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="is_published",
            field=models.BooleanField(default=True, verbose_name="Опубликовано"),
        ),
        migrations.CreateModel(
            name="Version",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "version_number",
                    models.CharField(
                        help_text="Введите номер версии",
                        max_length=200,
                        verbose_name="Номер версии",
                    ),
                ),
                (
                    "version_name",
                    models.CharField(
                        help_text="Введите название версии",
                        max_length=200,
                        verbose_name="Название версии",
                    ),
                ),
                ("sign", models.BooleanField(verbose_name="Признак текущей версии")),
                (
                    "product",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="product",
                        to="catalog.product",
                        verbose_name="продукт",
                    ),
                ),
            ],
            options={
                "verbose_name": "версия",
                "verbose_name_plural": "версии",
                "ordering": ["product", "version_number", "version_name", "sign"],
            },
        ),
    ]
