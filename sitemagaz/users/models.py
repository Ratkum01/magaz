from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    images= models.ImageField(upload_to='user_images', blank=True, null=True, verbose_name='Аватар')

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name= 'Пользователь'
        verbose_name_plural= 'Пользователи'