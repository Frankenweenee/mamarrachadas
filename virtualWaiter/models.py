
from django.db import models

# Create your models here.

class Categoria(models.Model):
    categoria=models.CharField( max_length=40)
 
    def __str__(self):
        return self.categoria


class Iva(models.Model):
    tipo_de_iva=models.CharField( max_length=50)
    porcentual=models.FloatField()

    def __str__(self):
        return self.tipo_de_iva

class Articulos(models.Model):
    articulo = models.CharField( max_length=40)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    precio = models.FloatField()
    iva = models.ForeignKey(Iva,on_delete=models.CASCADE)
    def __str__(self):
        return self.articulo
