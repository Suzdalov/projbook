from django.db import models
import uuid
from django.utils import timezone
# Create your models here.


class Project(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    dateStart = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name