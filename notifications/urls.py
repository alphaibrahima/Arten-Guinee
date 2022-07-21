from django.contrib import admin
from django.urls import path, include
from notifications.views import ShowNotifications, DeleteNotification



urlpatterns = [
    path('', ShowNotifications, name='show-notifications'),
    path('<noti_id>/delete', DeleteNotification, name='delete-notification')
]