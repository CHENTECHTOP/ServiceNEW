from django.db import models

class DeviceRepair(models.Model):
    model_name = models.CharField(max_length=150, verbose_name="Модель пристрою")
    features = models.CharField(max_length=255, verbose_name="Особливості", blank=True)
    problem = models.TextField(verbose_name="Опис проблеми")
    phone_number = models.CharField(max_length=20, verbose_name="Номер телефону")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата заявки")

    def __str__(self):
        return f"{self.model_name} - {self.phone_number}"