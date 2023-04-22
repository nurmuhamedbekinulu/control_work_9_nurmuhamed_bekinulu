from django.db import models
from django.contrib.auth.models import User


class Photo(models.Model):
    photo = models.ImageField(
        null=False,
        blank=False,
        verbose_name='Фотография'
    )
    caption = models.CharField(
        max_length=200,
        verbose_name='Название фотографии'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата и время создания"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата и время обновления"
    )
    author = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        verbose_name="Автор"
    )
    users = models.ManyToManyField(
        through='webapp.Favorite',
        to=User,
        related_name='photos'
    )

    def __str__(self):
        return f'{self.photo} - {self.caption}'
