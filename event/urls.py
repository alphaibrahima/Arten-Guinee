from django.contrib import admin
from django.urls import path, include
from .views import *
# from . import views







urlpatterns = [
    path('addevens', EvensViews.as_view(), name='addevens'),
    path("sup/<int:id>", DelEvent, name='delevent'),
    path('datas', sommeUser, name='datas'),
]