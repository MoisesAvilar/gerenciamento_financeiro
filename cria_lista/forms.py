from django import forms
from cria_lista.models import Item, Lista


class CadastraItensForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ('nome', 'quantidade', 'valor',)
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'autofocus': 'autofocus'}),
            'quantidade': forms.NumberInput(attrs={'class': 'form-control'}),
            'valor': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class CriaListaForm(forms.ModelForm):

    class Meta:
        model = Lista
        fields = ('nome', 'tipo', 'categoria', 'meta_de_gastos',)
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'autofocus': 'autofocus'}),
            'tipo': forms.Select(attrs={'class': 'form-select'}),
            'categoria': forms.Select(attrs={'class': 'form-select'}),
            'meta_de_gastos': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class AtualizaNomeListaForm(forms.ModelForm):

    class Meta:
        model = Lista
        fields = ('nome', 'tipo', 'categoria', 'meta_de_gastos',)
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'autofocus': 'autofocus'}),
            'tipo': forms.Select(attrs={'class': 'form-select'}),
            'categoria': forms.Select(attrs={'class': 'form-select'}),
            'meta_de_gastos': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class EditarItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ('nome', 'quantidade', 'valor',)
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'autofocus': 'autofocus'}),
            'quantidade': forms.NumberInput(attrs={'class': 'form-control'}),
            'valor': forms.NumberInput(attrs={'class': 'form-control'}),
        }
