from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    number_of_phone = models.CharField(max_length=20, blank=True, null=True)
    avatar = models.ImageField(upload_to='images/users/avatar/', blank=True, null=True, default='images/users/avatar/defolt/defolt_avatar.png')
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
