from django.db import models


# Create your models here.

class Curso(models.Model):
    nombre=models.CharField(max_length=50)
    comision=models.IntegerField()
    def __str__(self):
        return f"{self.nombre} - {self.comision}"

class Estudiante(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()
    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.email}"

class Profesor(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()
    profesion=models.CharField(max_length=50)
    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.email} - {self.profesion}"

class Entregables(models.Model):
    nombre=models.CharField(max_length=50)
    fecha=models.DateField()
    entregado=models.BooleanField()
    def __str__(self):
        return f"{self.nombre} - {self.fecha}"
    
class Sedes(models.Model):
    nombre=models.CharField(max_length=50)
    direccion=models.CharField(max_length=50)
    telefono=models.IntegerField()

    