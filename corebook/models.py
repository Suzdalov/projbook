from django.db import models
import uuid
from django.utils import timezone
# Create your models here.


class PjUser(models.Model):
    NickName = models.CharField(max_length=40, blank=True)
    UsrRef = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.NickName


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

