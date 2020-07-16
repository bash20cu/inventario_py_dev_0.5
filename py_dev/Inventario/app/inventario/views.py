from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Pieza, RegistroVenta, Categoria
from django.views.generic import ListView
from .forms import VentaForm, PiezaVenta

def home(request):
    return render(request, 'base.html')


    
def busqueda(request):
    if 'buscar' in request.GET and request.GET['buscar']:
        buscar = request.GET['buscar']
        pieza = Pieza.objects.filter(nombre__icontains=buscar)
        return render(request, 'busqueda.html', {'pieza': pieza, 'query': buscar})


def inventario(request):
    piezas = Pieza.objects.all()
    return render(request, 'inventario.html', {'piezas':piezas})


class ListaPiezas(ListView):
    model = Pieza
    template_name = 'inventario/piezas_list.html'


class ListaVenta(ListView):
    model = RegistroVenta
    template_name = 'inventario/registro_ventas.html'


def detalles(request, id):
    if request.method == 'GET':
        detalles = Pieza.objects.get(id=id)        
        return render(request, 'inventario/venta_form.html', {'detalles': detalles})

    if request.method == 'POST':
        detalles = Pieza.objects.get(id=id)
        cantidad = int(request.POST['cantidad'])
        precio_total = cantidad * float(detalles.precio)
        fecha = request.POST['fecha']
        if cantidad > detalles.cantidad:
            return render(request, 'inventario/venta_form.html', {'error': True, 'detalles': detalles})
        registro_venta = RegistroVenta.objects.create(cantidad=cantidad, pieza_id=detalles.id, fecha=fecha, precio=precio_total)
        detalles.cantidad = detalles.cantidad - cantidad
        registro_venta.save()
        detalles.save()
        return render(request, 'inventario/venta_validada.html', {'detalles': detalles})


def crudVentas(request):
    if request.method == 'POST':
        form = PiezaVenta(request.POST)
        if form.is_valid():
            form.save
        else:
            print('Hay Errores de formualrio')
            return HttpResponseRedirect(reverse('lista_piezas'))
    else:
        contexto = {'form': VentaForm()}
        return render(request, 'inventario/venta_validada.html', contexto)


def updateVentas(request,pk):
    venta = get_object_or_404(models.RegistroVenta, pk=pk)
    if request.method == 'POST':
        form = VentaForm(request.POST, instance=venta)
        if form.is_valid():
            form.save()
        else:
            print('Hay errores en el form')
            return HttpResponseRedirect(reverse('lista-piezas'))
    else:
        contexto = {'form': VentaForm(instance=venta)}
        return render(request, 'venta_validada.html', contexto)



    """"
    def detalles(request, id):
    if request.method == 'GET':
        detalles = Pieza.objects.get(id=id)
        return render(request, 'inventario/venta_form.html', {'detalles': detalles})
    
        if request.method == 'POST':
           detalles = Pieza.objects.get(producto_id=producto_id)
           cantidad = int(request.POST['cantidad'])
           precio_total = cantidad * float(detalles.precio)
           fecha = request.POST['fecha']
           registro_venta = RegistroVenta.objects.create(cantidad=cantidad, producto_id=producto_id, categoria_id=detalles.categoria_id, fecha=fecha, precio=precio_total, precio_venta=detalles.precio_venta)
           detalles.cantidad = detalles.cantidad - cantidad
           registro_venta.save()
           detalles.save()
           return render(request, 'inventario/venta_validada.html', {'detalles': detalles})

       """

