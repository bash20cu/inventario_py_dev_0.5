from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from datetime import datetime, timedelta
from inventario.models import Pieza, RegistroVenta, Categoria
from servicio.models import Servicio
from django.db.models import Sum
from django.contrib.admin.models import LogEntry


def reportes(request):
    if request.method == 'GET':
        categoria = Categoria.objects.all()
        baja = Pieza.objects.filter(cantidad='0')
        hoy = datetime.now()
        mes = hoy - timedelta(30)
        fecha_mas = RegistroVenta.objects.filter(fecha__range=(mes, hoy)).order_by('pieza', '-fecha')
        suma_fecha = fecha_mas.aggregate(Sum('precio'))
        cantidad_mas = RegistroVenta.objects.filter(cantidad__gte='5').order_by('-fecha')
        tsemana = hoy - timedelta(7)
        semana = Servicio.objects.filter(fecha__range=(tsemana, hoy)).order_by('-fecha')
        contexto = {'categoria': categoria, 'baja': baja, 'cantidad': cantidad_mas, 'fecha': fecha_mas, 'semana': semana, 'suma_total': suma_fecha['precio__sum']}
        return render(request, 'reportes.html', contexto)

    if request.method == 'POST':
        categoria = request.POST['categoria']
        lista = Pieza.objects.filter(categoria=categoria)
    return render(request, 'reportes/listado_categoria.html', {'lista': lista})

def reporte_cero(request):
    hoy = datetime.now()
    baja = Pieza.objects.filter(cantidad='0')
    return render(request, 'reportes.html', {'baja': baja,})

def reporte_venta_mes(request):
    hoy = datetime.now()
    mes = hoy - timedelta(30)
    fecha_mas = RegistroVenta.objects.filter(fecha__range=(mes, hoy)).order_by('pieza', '-fecha')
    suma_fecha = fecha_mas.aggregate(Sum('precio'))
    return render(request, 'reportes.html', {'fecha': fecha_mas, 'suma_total': suma_fecha['precio__sum']})


def reporte_servicio(request): 
    hoy = datetime.now()   
    tsemana = hoy - timedelta(7)
    semana = Servicio.objects.filter(fecha__range=(tsemana, hoy)).order_by('-fecha')
    return render(request, 'reportes.html', {'semana': semana})


def reporte_categoria(request):
    if request.method == 'GET':
        categoria = Categoria.objects.all()
        return render(request, 'reporte_categoria.html', {'categoria': categoria})

    if request.method == 'POST':
        categoria = request.POST['categoria']
        lista = Pieza.objects.filter(categoria=categoria).order_by('nombre')
    return render(request, 'listado_categoria.html', {'lista': lista})


def reporte_fecha(request):
    if request.method == 'GET':
        categoria = Categoria.objects.all()
        return render(request, 'reporte_fecha.html', {'categoria': categoria})

    if request.method == 'POST':
        fecha_inic = request.POST['fecha_inic']
        fecha_final = request.POST['fecha_final']
        lista = RegistroVenta.objects.filter(fecha__range=(fecha_inic, fecha_final)).order_by('-fecha')
        suma_pieza = lista.aggregate(Sum('precio'))
        lista_servicio = Servicio.objects.filter(fecha__range=(fecha_inic, fecha_final)).order_by('-fecha')
        suma_serv = lista_servicio.aggregate(Sum('precio'))
        contexto = {'lista': lista, 'suma_pieza': suma_pieza['precio__sum'], 'lista_servicio': lista_servicio, 'suma_servicio': suma_serv['precio__sum']}
    return render(request, 'listado_fecha.html', contexto)