from django.db import models
import datetime


class Car(models.Model):
    car_title = models.CharField("название автомобиля", max_length=50)
    car_year = models.CharField("год выпуска", max_length=50)
    car_mileage = models.CharField("пробег автомобиля", max_length=50)
    car_description = models.TextField("описание автомобиля")
    car_price = models.CharField("стоимость автомобиля", max_length=50)
    
    def __str__(self):
        return self.car_title
    
    class Meta:
        verbose_name = 'автомобиль'
        verbose_name_plural = 'автомобили'
