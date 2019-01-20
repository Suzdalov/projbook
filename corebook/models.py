from django.db import models
import uuid
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickName = models.CharField(max_length=40, blank=True)

    def __str__(self):
        return self.NickName


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Project(models.Model):
    projectId = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    dateStart = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey('PjUser', on_delete=models.CASCADE, related_name="fromProject")

    def __str__(self):
        return self.name

class PjItem(models.Model):
    itemId = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return(self.name)

