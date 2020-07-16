from django.db import models
from django.urls import reverse

# Create your models here.


class customFloatField(models.Field):
    def db_type(self, connection):
        return 'float'


class Servicio(models.Model):
    servicio_id = models.AutoField(primary_key=True)
    servicio = models.CharField(max_length=100, null=True, blank=True)
    cantidad = models.IntegerField()
    fecha = models.DateField()
    precio = models.DecimalField(default=0.00, max_digits=5, decimal_places=2)
    comentario = models.TextField(max_length=500, null=True, blank=True)

    def __unicode__(self):
        return self.servicio

    def get_absolute_url(self):
        return reverse('reporte_servicio')