# Generated by Django 5.1.1 on 2024-09-19 16:51

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0002_rename_prise_product_price"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="manufactured_at",
            field=models.DateTimeField(
                default=django.utils.timezone.now, verbose_name="Дата производства"
            ),
            preserve_default=False,
        ),
    ]
