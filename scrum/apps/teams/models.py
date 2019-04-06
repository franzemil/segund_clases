from django.db import models


class Equipo(models.Model):
    nombre = models.CharField(max_length=140)
    fecha_creacion = models.DateTime(auto_now_add=True)
