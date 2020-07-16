from django.conf.urls import url
from inventario.views import home
from servicio.views import servicio
from servicio.forms import ServicioForm


urlpatterns = [
    url(r'^$', home, name='home'),   
    url(r'^servicio/$', ServicioForm.as_view(), name='nuevo-servicio'),]