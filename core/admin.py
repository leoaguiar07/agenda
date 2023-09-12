from django.contrib import admin
from core.models import Evento

# Register your models here.

# Título das listas (listagem de registros)
class EventoAdmin(admin.ModelAdmin):
    # Título das listas (listagem de registros)
    list_display = ('titulo','data_evento', 'data_criacao')
    # crai campo de filtro e aponta o campo para filtar
    list_filter = ('usuario','data_evento',)



admin.site.register(Evento, EventoAdmin)