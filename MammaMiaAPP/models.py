from django.db import models

# Create your models here.

class Menu(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.PositiveIntegerField(default=0)
    descripcion = models.CharField(max_length=300)

    class Meta:
        permissions = [
            ("can_view_menu", "Can view menu"),
            ("can_edit_menu", "Can edit menu"),
        ]

    def __str__(self):
        return f"{self.nombre}"



class Plato(models.Model):
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    orden =  models.IntegerField(default = 0)
    imagenPlato = models.URLField(max_length=60, null=True, blank=True)
    menu = models.ForeignKey(Menu, related_name='platos', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        permissions = [
            ("can_view_plato", "Can view plato"),
            ("can_edit_plato", "Can edit plato"),
        ]

    def __str__(self):
        return f"{self.nombre}"


class Ingrediente(models.Model):
    nombre = models.CharField(max_length=50)
    alergeno = models.CharField(max_length=50)
    categoria = models.CharField(max_length=50)
    plato = models.ManyToManyField(Plato, related_name='ingredientes')

    class Meta:
        permissions = [
            ("can_view_ingrediente", "Can view ingrediente"),
            ("can_edit_ingrediente", "Can edit ingrediente"),
        ]
    
    def __str__(self):
        return f"{self.nombre}" 
