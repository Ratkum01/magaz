from email.policy import default
from turtle import mode
from unicodedata import category
from django.db import models

# Create your models here.
class Categories (models.Model):
    name= models.CharField(max_length=50, unique=True, verbose_name="Название")
    slug= models.SlugField(max_length=100, unique= True, blank=True , null= True , verbose_name='URL')

    class Meta:
        verbose_name= 'Категорю'
        verbose_name_plural= 'Категории'
class Product (models.Model):
    name= models.CharField(max_length=50, unique=True, verbose_name="Название")
    slug= models.SlugField(max_length=100, unique= True, blank=True , null= True , verbose_name='URL')
    description= models.TextField(default='Тут Пусто',verbose_name='Описание' )
    image= models.ImageField(upload_to='goods_images', blank=True, null=True,verbose_name='Изоброжение' )
    price= models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name="Цена")
    discount= models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name="Скидка в %")
    quantity=models.PositiveBigIntegerField(default=0,verbose_name= "Количество" )
    category=models.ForeignKey(to=Categories,on_delete= models.CASCADE, verbose_name='Категория' )


    class Meta:
        verbose_name= 'Продукт'
        verbose_name_plural= 'Продукты'