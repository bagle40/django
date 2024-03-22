from django.db import models
from django.urls import reverse

# Create your models here.



class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Название")
    slug = models.SlugField(
        max_length=200, unique=True, blank=True, null=True, verbose_name="URL")
    

    class Meta:
        db_table = "category"
        verbose_name = "Категорию"
        verbose_name_plural = "Категории"
    
    def __str__(self):
        return self.name



class Products(models.Model):
    shoes = 'shoes'
    Outerwear = 'Outerwear'
    t_shirts = 't_shirts'
    trousers='trousers'
    Costumes='Costumes'
    Sportswear='Sportswear'
    Accessories='Accessories'
    Dresses='Dresses'
    Overalls='Overall'
    sundresses='sundresses'
    no_sub_categories='---'

    LEVEL_CHOICES = (
        (no_sub_categories, '---'),
        (shoes, 'Обувь'),
        (Outerwear, 'Верхняя одежда'),
        (t_shirts, 'Футболки'),
        (trousers,'брюки'),
        (Costumes,'Костюмы'),
        (Sportswear,'Спортивная одежда'),
        (Accessories,'Аксессуары'),
        (Dresses,'Платья'),
        (Overalls,'Комбинезоны'),
        (sundresses,'сарафаны')
    )
    name = models.CharField(max_length=150, unique=True, verbose_name="Название")
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name="URL")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    mini_description = models.TextField(blank=True, null=True, verbose_name="Мини описание")
    image = models.ImageField(
        upload_to="goods_image", blank="True", null=True, verbose_name="Изображение"
    )
    price = models.DecimalField(
        default=0.00, max_digits=7, decimal_places=2, verbose_name="Цена"
    )
    discount = models.DecimalField(
        default=0.00, max_digits=7, decimal_places=2, verbose_name="Цена со скидкой"
    )
    quantity = models.PositiveIntegerField(default=0, verbose_name="Количество")
    category = models.ForeignKey(
        to=Categories, on_delete=models.CASCADE, verbose_name="Категория"
    )
    sub_category = models.CharField(max_length=150, choices=LEVEL_CHOICES, default=no_sub_categories,verbose_name="Подкатегория")
    articul=models.CharField(max_length=5,unique=True,verbose_name='Артикул')
    country=models.CharField(max_length=150,blank=True,verbose_name='Страна производства')
    size=models.CharField(max_length=2,blank=True,verbose_name='Размер')
    structure=models.CharField(max_length=400,blank=True,verbose_name='Состав')
    color=models.CharField(max_length=100,blank=True,verbose_name='Цвет')
    brand=models.CharField(max_length=100,blank=True,verbose_name='Бренд')


    class Meta:
        db_table = "product"
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering=("id",)
    
    def __str__(self):
        return f'{self.name} Количество - {self.quantity}'
    
    def get_absolute_url(self):
        return reverse("catalog:product", kwargs={"product_slug": self.slug})
    