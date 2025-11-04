from django.contrib import admin
from .models import Categoria, Lista, Transacao


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nome", "user")
    list_filter = ("user",)
    search_fields = ("nome", "user__username")


@admin.register(Lista)
class ListaAdmin(admin.ModelAdmin):
    list_display = ("nome", "user", "meta", "data")
    list_filter = ("user", "data")
    search_fields = ("nome", "user__username")
    filter_horizontal = ("shared_with",)
    autocomplete_fields = ("user",)


@admin.register(Transacao)
class TransacaoAdmin(admin.ModelAdmin):
    list_display = ("descricao", "valor", "user", "categoria", "lista", "data")
    list_filter = ("user", "lista", "categoria", "data")
    search_fields = ("descricao", "user__username", "lista__nome", "categoria__nome")
    autocomplete_fields = ("user", "categoria", "lista")
    list_per_page = 25
