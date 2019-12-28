from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Funcion(models.Model):
    pelicula = models.ForeignKey('Pelicula', on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin  = models.DateField()
    lugar = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    cupos = models.PositiveIntegerField()
    choices = (
    ("Disponible", "Disponible"),
    ("Cancelada", "Cancelada"),
  )
    estado = models.CharField(max_length=200,choices=choices, default="Disponible")

    class Meta():
        verbose_name_plural = 'Funciones'

    def evaluar(self, cupos_solicitados):
        self.cupos = self.cupos - cupos_solicitados
        self.save()

    def __str__(self):
        return "{}- {}-{}".format(self.pelicula,self.fecha_inicio,self.fecha_fin)

class Pelicula(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    director = models.CharField(max_length=200)
    genero = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Solicitud(models.Model):
    usuario = models.ForeignKey(User, on_delete="CASCADE")
    funcion = models.ForeignKey('Funcion', on_delete=models.CASCADE)
    num_boletas = models.PositiveIntegerField()
    
    def __str__(self):
        return "{}".format(self.id)