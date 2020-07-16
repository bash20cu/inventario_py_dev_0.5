from django.conf.urls import url
from inventario.views import home
from reportes.views import reportes,reporte_cero,reporte_venta_mes,reporte_servicio , reporte_categoria, reporte_fecha

urlpatterns = [    
    url(r'^reportes/$', reportes, name='reportes'),
    url(r'^reportes/cero$', reporte_cero, name='reporte_cero'),
    url(r'^reportes/venta_mes$', reporte_venta_mes, name='reporte_venta_mes'),
    url(r'^reportes/servicio$', reporte_servicio, name='reporte_servicio'),
    url(r'^reportes/categoria/$', reporte_categoria, name='reporte-categoria'),
    url(r'^reportes/fecha/$', reporte_fecha, name='reporte-fecha'),
]
