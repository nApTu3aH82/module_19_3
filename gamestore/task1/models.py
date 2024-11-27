from django.db import models


# Create your models here.
class Buyer(models.Model):
    name = models.CharField(max_length=100)  # Имя покупателя
    balance = models.DecimalField(max_digits=10, decimal_places=2)  # Количество денег
    age = models.IntegerField()  # Возраст

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=100)  # Название игры
    cost = models.DecimalField(max_digits=10, decimal_places=2)  # стоимость игры
    size = models.DecimalField(max_digits=10, decimal_places=2)  # размер файлов игры
    description = models.TextField(blank=True)  # описание игры
    age_limited = models.BooleanField()  # ограничение по возрасту
    buyer = models.ManyToManyField(Buyer, related_name='games')

    def __str__(self):
        return self.title

