from . import views
from django.urls import path
urlpatterns = [
    path('', views.index, name ='index'),
    path('invest/', views.invest, name = 'invest'),
    path('loan/', views.loan, name = 'loan'),
    path('btc/', views.btc, name = 'btc'),
    path('eth/', views.eth, name = 'eth')
    ]