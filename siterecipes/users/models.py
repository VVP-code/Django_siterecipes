from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    photo = models.ImageField(upload_to='user_photos/%Y/%m/%d/', null=True, blank=True, verbose_name='Фотография')
    date_of_birth = models.DateField(null=True, blank=True, verbose_name='Дата рождения')


