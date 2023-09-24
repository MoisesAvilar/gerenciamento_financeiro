from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

TIPO = (
    ('Prioritários', 'Prioritários'),
    ('Secundários', 'Secundários'),
    ('Luxo', 'Luxo'),
    ('Outros', 'Outros'),
)

CATEGORIA = (
    ('Compras-do-mes', 'Compras do mês'),
    ('Transporte', 'Transporte'),
    ('Lazer', 'Lazer'),
    ('Alimentacao-fora', 'Alimentação fora de casa'),
    ('Outros', 'Outros'),
)


class Lista(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50, null=False, blank=False)
    tipo = models.CharField(max_length=50, choices=TIPO, null=False, blank=False) # noqa
    categoria = models.CharField(max_length=50, choices=CATEGORIA, null=False, blank=False) # noqa
    data = models.DateField(auto_now_add=True)
    meta_de_gastos = models.DecimalField(
        decimal_places=2, max_digits=6, default=500, null=False, blank=False)

    @property
    def valor_total(self):
        total = 0
        for item in self.item_set.all():
            total += item.valor
        return total

    @property
    def calcular_diferenca(self):
        total = self.valor_total
        diferenca = self.meta_de_gastos - total
        return diferenca

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return f'lista/{self.id}/'


class Item(models.Model):
    lista = models.ForeignKey(Lista, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50,  null=False, blank=False)
    quantidade = models.IntegerField(default=1,  null=False, blank=False)
    valor = models.DecimalField(max_digits=6, decimal_places=2,  null=False, blank=False) # noqa

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('cria_lista:editar_item', args=[str(self.lista.id), str(self.id)]) # noqa
