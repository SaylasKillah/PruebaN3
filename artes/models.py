from django.db import models

# Create your models here.

class Producto(models.Model):
    idproducto=models.CharField(primary_key=True, max_length=8, verbose_name="Idproducto")
    producto=models.CharField(max_length=50, blank=True, verbose_name="Producto")
    precio=models.IntegerField(blank=True, null=True, verbose_name="Precio")
    imagen=models.ImageField(upload_to="imagenes", null=True, blank=True, verbose_name="Imagen")
    

    def __str__(self):
        return self.idproducto