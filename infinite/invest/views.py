from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import json 
import requests 

def index(request:HttpRequest)-> HttpResponse:
    context = {}
    return render(request, 'invest/index.html', context)



btc = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"

data = requests.get(btc) 
data = data.json() 
btc = data['price']

eth = "https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT"

data = requests.get(eth) 
data = data.json() 
eth = data['price']


def invest(request:HttpRequest)-> HttpResponse:
    btc = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"

    data = requests.get(btc) 
    data = data.json() 
    btc = data['price']

    eth = "https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT"

    data = requests.get(eth) 
    data = data.json() 
    eth = data['price']
    context = {'btc': btc, 'eth': eth}
    return render(request, 'invest/invest.html', context)

