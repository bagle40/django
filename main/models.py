from django.db import models


class Contact(models.Model):
    username=models.CharField(max_length=50,blank=True, null=True, verbose_name="Логин")
    e_mail=models.CharField(max_length=50,blank=True, null=True,verbose_name="E-mail")
    subject=models.CharField(max_length=100,blank=True, null=True, verbose_name="Тема")
    coment_text = models.TextField(null=True, blank=True, verbose_name="Сообщение")

    
    class Meta:
        db_table = "contact"
        verbose_name = "Обратная связь"
        verbose_name_plural = "Обратная связь"

    def __str__(self):
        return f"Оюращение № {self.pk} | Пользователь {self.username}"
    

class Mailing(models.Model):
    e_mail=models.CharField(max_length=50,unique=True,verbose_name="E-mail")

    class Meta:
        db_table = "mailing"
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылка"


    def __str__(self):
        return f"{self.e_mail}"
