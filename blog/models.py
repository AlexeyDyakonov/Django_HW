from django.db import models

NULLABLE = {"blank": True, "null": True}

class Blog(models.Model):
    title = models.CharField(
        max_length=150,
        verbose_name="Заголовок",
        help_text="Введите заголовок")

    slug = models.CharField(
        max_length=100,
        verbose_name="slug")

    content = models.TextField(
        verbose_name='содержимое',
        **NULLABLE
    )

    image = models.ImageField(
        upload_to="blog/image",
        verbose_name="Изображение",
        help_text="Загрузите изображение",
        **NULLABLE

    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания")


    is_published = models.BooleanField(
        default=True,
        verbose_name='Опубликовано'
    )

    view_counter = models.PositiveIntegerField(
        verbose_name="Счетчик просмотров",
        help_text="Укажите количество просмотров",
        default=0
    )

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
