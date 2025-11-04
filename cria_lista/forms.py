from django import forms
from django.utils import timezone
from django.db.models import Q
from .models import Categoria, Lista, Transacao


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ("nome",)
        widgets = {
            "nome": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ex: Supermercado, Gasolina, Salário",
                    "autofocus": "autofocus",
                }
            ),
        }

    def clean_nome(self):
        nome = self.cleaned_data.get('nome')
        if nome:
            return nome.capitalize()
        return nome


class ListaForm(forms.ModelForm):
    class Meta:
        model = Lista
        fields = (
            "nome",
            "meta",
        )
        labels = {
            "nome": 'Nome do "Envelope"',
            "meta": "Meta / Orçamento (opcional)",
        }
        widgets = {
            "nome": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ex: Orçamento da Casa, Férias",
                    "autofocus": "autofocus",
                }
            ),
            "meta": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Ex: 1500,00"}
            ),
        }

    def clean_nome(self):
        nome = self.cleaned_data.get('nome')
        if nome:
            return nome.capitalize()
        return nome


class TransacaoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        lista = kwargs.pop('lista', None)
        super().__init__(*args, **kwargs)

        if user and lista:
            q_user = Q(user=user)
            q_owner = Q(user=lista.user)
            q_used = Q(transacao__lista=lista)
            
            self.fields['categoria'].queryset = Categoria.objects.filter(
                q_user | q_owner | q_used
            ).distinct()
            
        elif user:
            self.fields['categoria'].queryset = Categoria.objects.filter(user=user)
        
        else:
            self.fields['categoria'].queryset = Categoria.objects.none()
            
        self.fields['data'].initial = timezone.now().date()

    class Meta:
        model = Transacao
        fields = ('valor', 'descricao', 'categoria', 'data')
        labels = {
            'valor': 'Valor (R$)',
            'descricao': 'Descrição',
            'categoria': 'Categoria',
            'data': 'Data da Transação',
        }
        widgets = {
            'valor': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '+150 (Renda) ou -50 (Gasto)',
                }
            ),
            'descricao': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ex: Gasolina, Salário',
                    'autofocus': 'autofocus'
                }
            ),
            'categoria': forms.Select(attrs={'class': 'form-select'}),
            'data': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }


class ShareListForm(forms.Form):
    identificador = forms.CharField(
        label="E-mail ou Nome de Usuário",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'usuario@exemplo.com ou nome_de_usuario'})
    )
