from django.db import models

# Create your models here.
from django.utils import timezone

class Usuario(models.Model):
    nombreCompleto = models.CharField(max_length=70)
    rut = models.CharField(max_length=10)
    email = models.CharField(max_length=65)
    telefono = models.CharField(max_length=20)
    region = models.CharField(max_length=70)
    comuna = models.CharField(max_length=50)
    fechaNacimiento = models.DateField()
    tipoVivienda = models.CharField(max_length=50)

    def __str__(self):
        return self.nombreCompleto

class Curso(models.Model):
    codigo=models.CharField(max_length=10)
    nombre=models.CharField(max_length=50)
    valor=models.IntegerField()
    def __str__(self):
        return self.nombre
    

class Alumno(models.Model):
    usuario = models.ForeignKey(Usuario, null=False, blank=False, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, null=False, blank=False, on_delete=models.CASCADE)
    fecha_matricula = models.DateField()
    activo = models.BooleanField() #Revisar
    def __str__(self):
        return self
