from django.contrib import admin
from .models import Client, User, Project
# Register your models here.
admin.site.register(Client)
admin.site.register(User)
admin.site.register(Project)