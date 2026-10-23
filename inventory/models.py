from django.db import models

class DeviceRepair(models.Model):
    model_name = models.CharField(max_length=150, verbose_name="Модель пристрою")
    features = models.CharField(max_length=255, verbose_name="Особливості", blank=True)
    problem = models.TextField(verbose_name="Опис проблеми")
    phone_number = models.CharField(max_length=20, verbose_name="Номер телефону")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата заявки")

    def __str__(self):
        return f"{self.model_name} - {self.phone_number}"

class Review(models.Model):
    author_name = models.CharField(max_length=100, verbose_name="Ім'я")
    rating = models.IntegerField(default=5, verbose_name="Оцінка (1-5)")
    text = models.TextField(verbose_name="Текст відгуку")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата")

    def __str__(self):
        return f"{self.author_name} ({self.rating}★)"