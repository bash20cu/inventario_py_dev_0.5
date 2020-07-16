from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View
from servicio.forms import ServicioForm
from .models import Servicio


def servicio(request):
    if request.method == 'GET':
        return render(request, 'servicio.html')


class Servicio(View):
    form_class = ServicioForm
    initial = {'key': 'value'}
    template_name = 'servicio_form.html'

    def get(self, request, *args, **kwargs):
        form = self.form_clas(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self,request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('/success/')
        return render(request, self.template_name, {'form': form})