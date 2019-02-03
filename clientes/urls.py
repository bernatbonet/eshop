# -*- encoding: utf-8 -*-
from django.conf.urls import include, url

from clientes import views

app_name = 'clientes'

urlpatterns = [
    url(r'^sujetos/', views.SujetoList.as_view()),
    url(r'^sujetos/<int:pk>/', views.SujetoDetail.as_view()),
    url('', views.api_root),
]