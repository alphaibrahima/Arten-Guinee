from django.db import models
from utilisateurs.models import User
from django.urls import reverse

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from notifications.models import Notification



class Message(models.Model):
    sender = models.ForeignKey(User, related_name="sender", on_delete=models.CASCADE)
    reciever = models.ForeignKey(User, related_name="reciever", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    contenu   = models.TextField()


    def __str__(self):
        return f"{self.sender } To {self.reciever} --- {self.timestamp.date()}"


    def user_message(sender, instance, *args, **kwargs):
        msg  = instance
        sender = msg.sender
        user = msg.reciever
        text_preview = msg.contenu[:15]

        notify = Notification(sender=sender, user=user, text_preview=text_preview, notification_type=3)
        notify.save()

#Signals for message
post_save.connect(Message.user_message, sender=Message)

