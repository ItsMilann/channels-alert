import logging
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model


MESSAGE = "You have received a new notification"
USR = get_user_model()


class Notifications(models.Model):
    user = models.ForeignKey(
        USR, on_delete=models.CASCADE, blank=True, null=True)
    text = models.CharField(max_length=255, default=MESSAGE)
    read = models.BooleanField(default=False)
    redirect = models.CharField(max_length=2083, default="/")

    def __str__(self):
        return self.text

    @property
    def unread_count(self):
        return self.__class__.objects.filter(user=self.user).count()


def notification_receiver(sender, instance, created, *args, **kwargs):
    if created:
        group = "notification"
        if instance.user:
            username = getattr(instance.user, instance.user.USERNAME_FIELD)
            group += f"-{username}"
        channel_layer = get_channel_layer()
        logging.critical(f"SCOPE {channel_layer}")
        assert channel_layer != None, "Channel layer is None."
        async_to_sync(channel_layer.group_send)(group, {
            "type": "new.notification",
            "event": "Notification",
            "text": instance.text,
            "redirect_url": instance.redirect,
            "unread_count": instance.unread_count,
        })


post_save.connect(notification_receiver, sender=Notifications)
