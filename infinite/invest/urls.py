from . import views
from django.urls import path
urlpatterns = [
    path('', views.index, name ='index'),
    path('invest/', views.invest, name = 'invest'),
    ]