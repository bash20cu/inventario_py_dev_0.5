from django import forms
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from servicio.models import Servicio


class ServicioForm(CreateView):
    model = Servicio
    fields = ['servicio', 'cantidad', 'fecha', 'precio', 'comentario']
    widgets = {'servicio': forms.TextInput(attrs={'class': 'form-control'}),
               'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
               'precio': forms.NumberInput(attrs={'class': 'form-control'}),
               'fecha': forms.DateInput(attrs={'class': 'form-control'})}

