from django.db import models
from django.utils.translation import gettext_lazy as _
import requests

class Btc(models.Model):
    
    name = models.CharField(max_length=100)
    ammount = models.FloatField(null=True)
    btc = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    data = requests.get(btc) 
    data = data.json() 
    btc = data['price']

    def __str__(self):
        return self.name, self.ammount
    

class Eth(models.Model):
    
    name = models.CharField(max_length=100)
    ammount = models.FloatField(null=True)
    eth = "https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT"
    data = requests.get(eth) 
    data = data.json() 
    eth = data['price']

    def __str__(self):
        return self.name, self.ammount