from django import forms
from cria_lista.models import Item, Lista


class CadastraItensForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('nome', 'quantidade', 'valor',)


class CriaListaForm(forms.ModelForm):
    class Meta:
        model = Lista
        fields = ('nome', 'tipo', 'categoria', 'meta_de_gastos',)


class AtualizaNomeListaForm(forms.ModelForm):
    class Meta:
        model = Lista
        fields = ('nome', 'tipo', 'categoria', 'meta_de_gastos',)


class EditarItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('nome', 'quantidade', 'valor',)
