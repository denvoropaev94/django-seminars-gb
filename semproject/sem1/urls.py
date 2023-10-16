from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('eagle/', eagle, name='eagle'),
    path('coin/', coin, name="coin"),
    path('last_coins/', last_coins, name="last_coins")
]
