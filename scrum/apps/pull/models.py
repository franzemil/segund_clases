from django.db import models
from django.contrib.auth.models import User


class Opcion(models.Model):
    """
    Cada Opciones que contendra una pregunta
    Extends:
        models.Model

    Variables:
        descripcion {CharField} -- Descripcion de la opcion
    """
    descripcion = models.CharField(max_length=140)


class Pregunta(models.Model):
    """
    Las preguntas que estaran disponibles en cada encuesta

    Extends:
        models.Model

    Variables:
        descripcion {CharField} -- Nombre de la encuesta
        opciones {Opcion[]} -- Lista de Opciones disponibles
        respuestas {Opcion[]} -- Lista de Opciones Basicas
        multiple_choice {BooleanField} -- True en casi que se adminan multiples respuestas
    """
    descripcion = models.CharField(max_length=140)
    opciones = models.ForeignKey(Opcion, related_name='+', on_delete=models.PROTECT)
    respuestas = models.ForeignKey(Opcion, related_name='+', on_delete=models.PROTECT)
    multiple_choice = models.BooleanField(default=True)


class Encuesta(models.Model):
    """
    Colleccion de Pregunttas las cuales seran publicadas

    Extends:
        models.Model

    Variables:
        nombre {CharField} -- Nombre con le cual se publicara la encuesta
        fecha_creacion {DateTimeField} -- Fecha de creacion de la encuesta
        participantes {User[]} -- Lista de Usuario los cuales podran acceder a la encuesta
        preguntas {Pregunta[]} --  Lista de Pregutnas las cuales se publicaran
        fecha_publicacion {DateTimeField} -- Fecha que indica a partir
    """
    nombre = models.CharField(max_length=140)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    participantes = models.ManyToManyField(User, related_name='encuestas', on_delete=models.PROTECT)
    preguntas = models.ManyToManyField(Pregunta, related_name='+', on_delete=models.PROTECT)
    fecha_publicacion = models.DateTimeField(null=True, blank=True)


class ResultadoPregunta(models.Model):
    """
    Resultado de una pregunta pro parte de un usuario
    [description]

    Extends:
        models.Model

    Variables:
        pregunta {[type]} -- [description]
        opcion {[type]} -- [description]
    """
    pregunta = models.ForeignKey(Pregunta, related_name='+', on_delete=models.PROTECT)
    opcion = models.ForeignKey(Opcion, related_name='+', on_delete=models.PROTECT)


class ResultadoEncuesta(models.Model):
    encuesta = models.ForeignKey(Encuesta, related_name='+', on_delete=models.PROTECT)
    usuario = models.ForeignKey(User, related_name='+', on_delete=models.PROTECT)
    resultados = models.ForeignKey(ResultadoPregunta, related_name='+', on_delete=models.PROTECT)
