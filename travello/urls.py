from django.conf import settings
from django.contrib import admin
from django.urls import path
from .import views
from django.urls import path, include
from django.conf.urls.static import static



urlpatterns = [
    path('', views.index,name='index'),

]

