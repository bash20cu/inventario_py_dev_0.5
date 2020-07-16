from django.conf.urls import include, url
from . import views
from .views import inventario, busqueda, ListaPiezas, ListaVenta,detalles, crudVentas
#from django.url import path



urlpatterns = [  
	url(r'^$', views.home),  
    url(r'^inventario/$', inventario, name='inventario'),
    url(r'^buscar/$', busqueda, name='buscar'),
    url(r'^inventario/piezas/$', ListaPiezas.as_view(), name='lista_piezas'),
    url(r'^inventario/detalles/(?P<id>\d+)/$', detalles, name='venta-piezas'),
    url(r'^inventario/validado/$', crudVentas, name='venta'),
    url(r'^inventario/ventas/$', ListaVenta.as_view(), name='lista-venta'),
]