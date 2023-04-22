from django.contrib.auth.models import User
from django.db import models

from webapp.models import Photo


class Favorite(models.Model):
    user = models.ForeignKey(
        to=User,
        related_name='favorite_users',
        verbose_name='Избранное',
        null=False,
        on_delete=models.CASCADE
    )
    photo = models.ForeignKey(
        to=Photo,
        related_name='favorite_photos',
        verbose_name='Избранное',
        null=False,
        on_delete=models.CASCADE
    )
    note = models.CharField(
        max_length=50,
        verbose_name='Текстовая заметка',
        null=False,
        blank=True
    )

    class Meta:
        verbose_name = 'Избранная фотография',
        verbose_name_plural = 'Избранные фотографии'
