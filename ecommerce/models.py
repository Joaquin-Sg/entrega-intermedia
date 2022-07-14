from django.db import models

# Create your models here.

class Producto(models.Model):
    name_of_product = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    details = models.TextField()
    image = models.CharField(max_length=5000, null=True, blank=True)

class Usuario(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    edad = models.IntegerField()


