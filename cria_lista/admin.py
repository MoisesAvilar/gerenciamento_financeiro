from django.contrib import admin
from cria_lista.models import Lista, Item


class ItemAdmin(admin.ModelAdmin):
    list_display = ('lista', 'nome', 'valor',)
    list_filter = ('nome',)


class ListaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo', 'categoria', 'data', 'meta_de_gastos',)
    list_filter = ('tipo', 'categoria',)


admin.site.register(Item, ItemAdmin)
admin.site.register(Lista, ListaAdmin)
