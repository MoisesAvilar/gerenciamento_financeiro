from django import forms
from cria_lista.models import Item, Lista


class CadastraItensForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('nome', 'quantidade', 'valor',)
        widgets = {
            'nome': forms.TextInput(attrs={'autofocus': 'autofocus'}),
        }


class CriaListaForm(forms.ModelForm):
    class Meta:
        model = Lista
        fields = ('nome', 'tipo', 'categoria', 'meta_de_gastos',)
        widgets = {
            'nome': forms.TextInput(attrs={'autofocus': 'autofocus'}),
        }


class AtualizaNomeListaForm(forms.ModelForm):
    class Meta:
        model = Lista
        fields = ('nome', 'tipo', 'categoria', 'meta_de_gastos',)
        widgets = {
            'nome': forms.TextInput(attrs={'autofocus': 'autofocus'}),
        }


class EditarItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('nome', 'quantidade', 'valor',)
        widgets = {
            'nome': forms.TextInput(attrs={'autofocus': 'autofocus'}),
        }
