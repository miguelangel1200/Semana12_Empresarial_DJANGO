from django.db import models

# Create your models here.

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=50)

class Libro(models.Model):
    id_autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    codigo = models.IntegerField(default=0)
    titulo = models.CharField(max_length=100)
    isbn = models.CharField(max_length=30)
    editorial = models.CharField(max_length=60)
    numpage = models.SmallIntegerField()


class Usuario(models.Model):
    num_usuario = models.IntegerField(default=0)
    nif = models.CharField(max_length=20)
    nombre_us = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    telefono = models.IntegerField(20)

class Prestamo(models.Model):
    id_libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fec_prestamo = models.DateField()
    fec_devolucion = models.DateField()
