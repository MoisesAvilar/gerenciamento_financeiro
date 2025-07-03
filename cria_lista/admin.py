# cria_lista/admin.py
from django.contrib import admin
from cria_lista.models import Lista, Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('lista', 'nome', 'valor',)
    list_filter = ('lista', 'nome',)


@admin.register(Lista)
class ListaAdmin(admin.ModelAdmin):
    # Adicione 'tipo' aqui
    list_display = ('nome', 'tipo', 'categoria', 'data', 'meta_de_gastos',)
    list_filter = ('tipo', 'categoria',)