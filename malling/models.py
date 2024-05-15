from django.db import models

# Create your models here.
class Mailing(models.Model):
    e_mail=models.CharField(max_length=50,unique=True,verbose_name="E-mail")
    subscribed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "mailing"
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылка"


    def __str__(self):
        return f"{self.e_mail}"