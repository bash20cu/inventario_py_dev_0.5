from django.contrib import admin
from .models import Pieza, Categoria, RegistroVenta

# Register your models here.

class PiezaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'cantidad', 'categoria')
    search_fields = ('nombre',)

    
admin.site.register(Categoria)
admin.site.register(Pieza, PiezaAdmin)
admin.site.register(RegistroVenta)