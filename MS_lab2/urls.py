"""MS_lab2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from Proj1 import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^lab2/', views.lab2 , name='lab2'),
    url(r'^show', views.show),
    url(r'^delete', views.delete),
    url(r'^update', views.update),
    url(r'^onl', views.onl),
    url(r'^create', views.create),
    url(r'^add', views.add),
    url(r'^load', views.load),
    url(r'^searchdigit', views.searchdigit),
]
