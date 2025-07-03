from django import forms
from cria_lista.models import Item, Lista


class CadastraItensForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = (
            "nome",
            "quantidade",
            "valor",
        )
        widgets = {
            "nome": forms.TextInput(
                attrs={"class": "form-control", "autofocus": "autofocus"}
            ),
            "quantidade": forms.NumberInput(attrs={"class": "form-control"}),
            "valor": forms.NumberInput(attrs={"class": "form-control"}),
        }


class CriaListaForm(forms.ModelForm):
    tipo = forms.ChoiceField(
        choices=Lista.TIPO_CHOICES,
        widget=forms.RadioSelect(attrs={"class": "btn-check"}),
        initial=Lista.TIPO_GASTO,
        label="Qual o tipo de lista?",
    )

    class Meta:
        model = Lista
        fields = (
            "nome",
            "tipo",
            "categoria",
            "meta_de_gastos",
        )
        widgets = {
            "nome": forms.TextInput(
                attrs={"class": "form-control", "autofocus": "autofocus"}
            ),
            "categoria": forms.Select(attrs={"class": "form-select"}),
            "meta_de_gastos": forms.NumberInput(attrs={"class": "form-control"}),
        }
        labels = {"meta_de_gastos": "Limite de Gastos / Valor da Dívida"}


class AtualizaNomeListaForm(forms.ModelForm):
    tipo = forms.ChoiceField(
        choices=Lista.TIPO_CHOICES,
        widget=forms.RadioSelect(attrs={"class": "btn-check"}),
        label="Qual o tipo de lista?",
    )

    class Meta:
        model = Lista
        fields = (
            "nome",
            "tipo",
            "categoria",
            "meta_de_gastos",
        )
        widgets = {
            "nome": forms.TextInput(
                attrs={"class": "form-control", "autofocus": "autofocus"}
            ),
            "categoria": forms.Select(attrs={"class": "form-select"}),
            "meta_de_gastos": forms.NumberInput(attrs={"class": "form-control"}),
        }
        labels = {"meta_de_gastos": "Limite de Gastos / Valor da Dívida"}


class EditarItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = (
            "nome",
            "quantidade",
            "valor",
        )
        widgets = {
            "nome": forms.TextInput(
                attrs={"class": "form-control", "autofocus": "autofocus"}
            ),
            "quantidade": forms.NumberInput(attrs={"class": "form-control"}),
            "valor": forms.NumberInput(attrs={"class": "form-control"}),
        }
