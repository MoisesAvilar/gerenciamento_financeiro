from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Lista(models.Model):
    TIPO_GASTO = "GASTO"
    TIPO_DIVIDA = "DIVIDA"
    TIPO_CHOICES = [
        (TIPO_GASTO, "Lista de Gastos"),
        (TIPO_DIVIDA, "Lista de Dívidas"),
    ]

    TIPO_CATEGORIA = (
        ("Prioritários", "Prioritários"),
        ("Secundários", "Secundários"),
        ("Luxo", "Luxo"),
        ("Outros", "Outros"),
    )

    CATEGORIA = (
        ("Compras-do-mes", "Compras do mês"),
        ("Transporte", "Transporte"),
        ("Lazer", "Lazer"),
        ("Alimentacao-fora", "Alimentação fora de casa"),
        ("Outros", "Outros"),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50, null=False, blank=False)

    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES, default=TIPO_GASTO)

    tipo_categoria = models.CharField(
        max_length=50,
        choices=TIPO_CATEGORIA,
        null=False,
        blank=False,
        default="Outros",
        name="tipo_categoria_gasto",
    )
    categoria = models.CharField(
        max_length=50, choices=CATEGORIA, null=False, blank=False
    )
    data = models.DateField(auto_now_add=True)
    meta_de_gastos = models.DecimalField(
        decimal_places=2, max_digits=10, default=500, null=False, blank=False
    )

    @property
    def valor_total(self):
        return sum((item.valor * item.quantidade) for item in self.item_set.all())

    @property
    def calcular_diferenca(self):
        if self.tipo == self.TIPO_DIVIDA:
            return self.meta_de_gastos - self.valor_total
        else:
            return self.meta_de_gastos - self.valor_total

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return f"lista/{self.id}/"


class Item(models.Model):
    lista = models.ForeignKey(Lista, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50, null=False, blank=False)
    quantidade = models.IntegerField(default=1, null=False, blank=False)
    valor = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, blank=False
    )
    added_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    @property
    def total(self):
        return self.quantidade * self.valor

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse(
            "cria_lista:editar_item", args=[str(self.lista.id), str(self.id)]
        )
