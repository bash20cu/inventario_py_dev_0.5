from django.conf.urls import include, url
#from django.url import path
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('inventario.urls')),
    url(r'', include('reportes.urls')),
    url(r'', include('servicio.urls')),
    # ... your url patterns
]