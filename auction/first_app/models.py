from django.db import models


class Car(models.Model):
    category = models.CharField(max_length=16, verbose_name='category')
    marka = models.CharField(max_length=16, verbose_name='marka')
    model = models.CharField(max_length=16, verbose_name='model')
    price = models.PositiveIntegerField(default=0, verbose_name='price')
    year = models.SmallIntegerField(default=2020, verbose_name='year')
    mileage = models.PositiveIntegerField(default=0, verbose_name='mileage')
    city = models.CharField(max_length=16, verbose_name='city')
    country = models.CharField(max_length=16, verbose_name='country')
    with_photo = models.BooleanField(default=True, verbose_name='with_photo')
    color = models.CharField(max_length=16, verbose_name='color')
    volume = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='volume')
    description = models.TextField(verbose_name='description')

    def __str__(self) -> str:
        return f"Model: {self.model} - Category: {self.category}"

class Bet(models.Model):
    number = models.IntegerField(verbose_name='number')
    total_number = models.IntegerField(verbose_name='total_nuber')
    buy_now = models.IntegerField(verbose_name='vuy_now')
    start_date = models.DateField(auto_now_add=True, verbose_name='start_date')
    end_date = models.DateField(auto_now_add=True, verbose_name='end_date')

    def __str__(self) -> str:
        return f"{self.number}"