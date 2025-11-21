from django import forms
from django.utils import timezone
from django.db.models import Q, Count
from .models import Categoria, Lista, Transacao
from django.forms import DateInput, ChoiceField, Select


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
            base_qs = Categoria.objects.filter(q_user | q_owner | q_used)
        elif user:
            base_qs = Categoria.objects.filter(user=user)
        else:
            base_qs = Categoria.objects.none()

        if self.instance.pk and self.instance.categoria:
            saved_category_qs = Categoria.objects.filter(pk=self.instance.categoria.pk)
            base_qs = base_qs | saved_category_qs

        self.fields['categoria'].queryset = base_qs.distinct().order_by('nome')

        self.fields['data'].initial = timezone.now().date()

    class Meta:
        model = Transacao
        fields = ('valor', 'descricao', 'categoria', 'data')
        help_texts = {
            'valor': 'Use - para gasto. Ex: -50',
        }
        labels = {
            'valor': 'Valor (R$)',
            'descricao': 'Descrição',
            'categoria': 'Categoria',
            'data': 'Data da Transação',
        }
        widgets = {
            'valor': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': ' ',
            }),
            'descricao': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': ' ',
            }),
            'categoria': forms.Select(attrs={
                'class': 'form-select',
            }),
            'data': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'placeholder': ' ',
            }, format='%Y-%m-%d'),
        }


class ShareListForm(forms.Form):
    identificador = forms.CharField(
        label="E-mail ou Nome de Usuário",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'usuario@exemplo.com ou nome_de_usuario'})
    )


class TransacaoFilterForm(forms.Form):
    PERIOD_CHOICES = [
        ('all', 'Todo o Período'),
        ('today', 'Hoje'),
        ('week', 'Últimos 7 dias'),
        ('month', 'Mês Atual'),
        ('custom', 'Período Personalizado'),
    ]

    ORDER_CHOICES = [
        ('newest', 'Mais Recentes'),
        ('oldest', 'Mais Antigas'),
        ('highest', 'Maior Valor'),
        ('lowest', 'Menor Valor'),
    ]
    
    periodo = ChoiceField(choices=PERIOD_CHOICES, required=False, label='Período', widget=Select(attrs={'class': 'form-select form-select-sm'}))
    ordem = ChoiceField(choices=ORDER_CHOICES, required=False, label='Ordenar por', widget=Select(attrs={'class': 'form-select form-select-sm'}))
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.none(), required=False, label='Categoria', widget=Select(attrs={'class': 'form-select form-select-sm'}))
    data_inicio = forms.DateField(required=False, label='De', widget=DateInput(attrs={'class': 'form-control form-control-sm', 'type': 'date'}))
    data_fim = forms.DateField(required=False, label='Até', widget=DateInput(attrs={'class': 'form-control form-control-sm', 'type': 'date'}))

    def __init__(self, *args, **kwargs):
        lista = kwargs.pop('lista', None)
        super().__init__(*args, **kwargs)
        
        if lista:
            q_user = Q(user=lista.user)
            q_shared = Q(transacao__lista=lista)
            
            self.fields['categoria'].queryset = Categoria.objects.filter(q_user | q_shared).distinct().order_by('nome')
            self.fields['categoria'].label = 'Categoria Ativa'
