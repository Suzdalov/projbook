from django.contrib import admin
from .models import Project, PjUser, PjItem

# Register your models here.
admin.site.register(Project)
admin.site.register(PjUser)
admin.site.register(PjItem)
