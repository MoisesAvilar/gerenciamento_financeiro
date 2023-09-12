from django import forms
from cria_lista.models import Item, Lista


class CadastraItensForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('nome', 'quantidade', 'valor',)


class CriaListaForm(forms.ModelForm):
    class Meta:
        model = Lista
        fields = '__all__'


class AtualizaNomeListaForm(forms.ModelForm):
    class Meta:
        model = Lista
        fields = '__all__'
    listas = forms.ModelChoiceField(queryset=Lista.objects.all())
    nome = forms.CharField(max_length=50)
