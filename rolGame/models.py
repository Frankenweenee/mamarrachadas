from django.db import models

# Create your models here.

class juego_rol(models.Model):
    tarea= models.CharField(max_length=40)
    descripcion_tarea = models.CharField(max_length=400)

    def __str__(self):
        return self.tarea

class nameDb(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name
