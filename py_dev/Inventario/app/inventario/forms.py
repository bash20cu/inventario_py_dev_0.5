from django import forms
from django.db import models
from django.forms import ModelForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Pieza, RegistroVenta


class PiezaVenta(CreateView):
        class Meta:
                model = RegistroVenta
                fields = ['cantidad', 'fecha']


class VentaForm(ModelForm):
    class Meta:
        model = RegistroVenta
        fields = '__all__'


"""
class BorrarPieza(DeleteView):
    model = Piezas
    success_url = reverse_lazy('lista-categoria')

class ActualizarPieza(UpdateView):
    model = Piezas


class EditarForm(forms.ModelForm):
    class Meta:
        model = Piezas
        fields = ['cantidad', 'producto', 'categoria','subcategoria', 'precio_venta', 'precio_costo','fecha_entrada']
        labels = {'cantidad': 'Cantidad', 'prodcuto': 'Producto', 'categoria': 'Categoria',
                  'precio_costo': 'Precio de Costo', 'precio_venta': 'Precio de Venta',
                  'fecha_entrada': 'Fecha de Entrada'}
        widgets = {'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
                   'producto': forms.TextInput(attrs={'class': 'form-control'}),
                   'categoria': forms.TextInput(attrs={'class': 'form-control'}),
                   'subcategoria': forms.TextInput(attrs={'class': 'form-control'}),
                   'precio_costo': forms.NumberInput(attrs={'class': 'form-control'}),
                   'precio_venta': forms.NumberInput(attrs={'class': 'form-control'}),
                   'fecha_entrada': forms.DateInput(attrs={'class': 'form-control'})}


"""