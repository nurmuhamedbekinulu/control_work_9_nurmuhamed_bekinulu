from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Photo(models.Model):
    photo = models.ImageField(
        null=False,
        blank=False,
        upload_to='user_photos',
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
    is_deleted = models.BooleanField(
        verbose_name='удалено',
        null=False,
        default=False
    )
    deleted_at = models.DateTimeField(
        verbose_name='Дата и время удаления',
        null=True,
        default=None
    )

    def __str__(self):
        return f'{self.photo} - {self.caption}'
    
    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()


    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фотографии'

