from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import json 
import requests 
from . import models

def index(request:HttpRequest)-> HttpResponse:
    context = {}
    return render(request, 'invest/index.html', context)

def invest(request:HttpRequest)-> HttpResponse:
    context = {'btc': models.Btc.btc, 'eth': models.Eth.eth}
    return render(request, 'invest/invest.html', context)

def loan(request:HttpRequest) -> HttpResponse:
    return render(request, 'invest/loan.html')

def btc(request:HttpRequest) -> HttpResponse:
    context = {'name' : models.Btc.objects.all()[0].name, 'ammount': models.Btc.objects.all()[0].ammount *float(models.Btc.btc)}
    return render(request, 'invest/btc.html', context )

def eth(request:HttpRequest) -> HttpResponse:
    context = {'name' : models.Btc.objects.all()[0].name, 'ammount': models.Eth.objects.all()[0].ammount *float(models.Eth.eth)}
    return render(request, 'invest/eth.html', context )