from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Group
from .models import estudiante, profesor, propuesta



admin.site.register(estudiante)
admin.site.register(profesor)
admin.site.register(propuesta)
