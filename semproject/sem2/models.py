from django.db import models
from django.utils import timezone


class SaveCoin(models.Model):
    coins = (('О', 'орел'), ('Р', 'решка'))
    coin_variant = models.CharField(max_length=1, choices=coins)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.coin_variant}'

    class Meta:
        ordering = ["-date"]

    @staticmethod
    def count_coins(n):
        return SaveCoin.objects.all()[:n]

