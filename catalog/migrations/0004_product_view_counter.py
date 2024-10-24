# Generated by Django 5.1.1 on 2024-10-12 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0003_alter_product_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="view_counter",
            field=models.PositiveIntegerField(
                default=0,
                help_text="Укажите количество просмотров",
                verbose_name="Счетчик просмотров",
            ),
        ),
    ]
