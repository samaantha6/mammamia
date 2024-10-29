from django.db import models

# Create your models here.

class Menu(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.PositiveIntegerField(default = 0)
    descripcion = models.CharField(max_length=300)


class Plato(models.Model):
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    orden =  models.IntegerField(default = 0)
    menu = models.ForeignKey(Menu, related_name='platos', on_delete=models.CASCADE)


class Ingrediente(models.Model):
    nombre = models.CharField(max_length=50)
    alergeno = models.CharField(max_length=50)
    categoria = models.CharField(max_length=50)
    plato = models.ForeignKey(Plato, related_name='ingredientes', on_delete=models.CASCADE)

