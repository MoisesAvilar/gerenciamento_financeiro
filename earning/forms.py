from django import forms
from earning.models import Earning


class EarningForm(forms.ModelForm):
    class Meta:
        model = Earning
        fields = ('earning', 'category',)
        widgets = {
            'earning': forms.NumberInput(attrs={
                'class': 'form-control',
                'autofocus': 'autofocus',
            }),
        }
