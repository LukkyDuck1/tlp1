from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class propuesta(models.Model):
    nombre= models.CharField(max_length=80, verbose_name="Nombre")
    
    descripcion= models.CharField(max_length=255, verbose_name="Descripcion")
    patrocinio = models.BooleanField(default=False)

    
    def __str__(self) -> str:
        return self.nombre




class estudiante(models.Model):
    nombre= models.CharField(max_length=80, verbose_name="Nombre")
    def __str__(self) -> str:
        return self.nombre
    


class profesor(models.Model):
    nombre= models.CharField(max_length=80, verbose_name="Nombre")

    def __str__(self) -> str:
        return self.nombre