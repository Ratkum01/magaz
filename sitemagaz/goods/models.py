from django.db import models

# Create your models here.
class Categories (models.Model):
    name= models.CharField(max_length=50, unique=True, verbose_name="Название")
    slug= models.SlugField(max_length=100, unique= True, blank=True , null= True , verbose_name='URL')

    class Meta:
        verbose_name= 'Категорю'
        verbose_name_plural= 'Категории'