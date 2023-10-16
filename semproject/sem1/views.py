from django.shortcuts import render
from django.http import HttpResponse
import random
import logging
from sem2.models import SaveCoin

logger = logging.getLogger(__name__)


def index(request):
    logger.info('Index page accessed!')
    return HttpResponse('Hello World!')


def eagle(request):
    num = (random.choice(['Глеб', 'Олег', 'Денис', 'Никита', 'Александр', 'Сергей']))
    return HttpResponse(f'<h1>Кто же пойдет на супер важное задание из отдела ДО?</h1><br><h2>И это будет - {num}</h2>')


def coin(request):
    rnd_coin = random.choice(['орел', 'решка'])
    save_coin = SaveCoin(coin_variant=rnd_coin)
    save_coin.save()
    return HttpResponse(rnd_coin)


def last_coins(request):
    stat = SaveCoin.count_coins(5)
    return HttpResponse(stat)
