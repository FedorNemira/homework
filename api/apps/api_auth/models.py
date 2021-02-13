from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    creation_date = models.DateTimeField("Дата последнего входа", auto_now_add=True)

    class Meta:
        verbose_name = ("Пользователи")
        verbose_name_plural = ("Пользователи")

    def __str__(self):
            return f'{self.user.username}'