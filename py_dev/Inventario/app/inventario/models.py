from django.db import models
from datetime import datetime
#from django.forms import ModelForm
#from django.urls import reverse


class Categoria(models.Model):
    categoria = models.CharField(max_length=30)
    seccion = models.CharField(max_length=100, null=True, blank=True)

    def __unicode__(self):
        return '{}'.format(self.categoria)


    class Meta:
        ordering = ["categoria", "seccion"]


class Pieza(models.Model):
    nombre = models.CharField(max_length=50, null=True, blank=True)
    cantidad = models.IntegerField(null=True, blank=True)
    categoria = models.ForeignKey(Categoria, null=True, blank=True, on_delete=models.SET_NULL)
    precio = models.DecimalField(default=0.00, max_digits=5, decimal_places=2)
    precio_venta = models.DecimalField(default=0.00, max_digits=5, decimal_places=2)
    fecha = models.DateField()
    
    class Meta:
        ordering = ["categoria"]

    def __unicode__(self):
        return format(self.nombre)



class RegistroVenta(models.Model):
    pieza = models.ForeignKey(Pieza, null=True, blank=True)
    cantidad = models.IntegerField(default=0)
    precio = models.DecimalField(default=0.00, max_digits=5, decimal_places=2)
    fecha = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ["-fecha"]

    def __unicode__(self):
        return '{}'.format(self.pieza)

    @property
    def importe(self):
        return self.pieza.precio * self.cantidad

    @property
    def suma_total(self):
        return self.cantidad * self.pieza.precio

