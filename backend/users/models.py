from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(
        'Электронная почта',
        unique=True,
        max_length=100
    )
    username = models.CharField(
        'Имя пользователя',
        unique=True,
        max_length=100
    )
    first_name = models.CharField(
        'Имя',
        max_length=100
    )
    last_name = models.CharField(
        'Фамилия',
        max_length=100)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', ]

    class Meta:
        ordering = ['id']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
