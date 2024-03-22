from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    phone=models.CharField(max_length=11,blank=True,verbose_name='Телефон')
    address=models.TextField(max_length=200,blank=True,verbose_name='Адрес')


    class Meta:
        db_table = "user"
        verbose_name = "Пользователя"
        verbose_name_plural = "Пользователи"
    
    def __str__(self):
        return self.username
