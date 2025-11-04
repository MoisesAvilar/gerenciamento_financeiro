from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.utils import timezone


class Categoria(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="categorias")
    nome = models.CharField(max_length=100)

    class Meta:
        unique_together = ("user", "nome")

    def __str__(self):
        return self.nome.capitalize()

    def save(self, *args, **kwargs):
        if self.nome:
            self.nome = self.nome.capitalize()
        super().save(*args, **kwargs)


class Lista(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="listas_criadas"
    )
    shared_with = models.ManyToManyField(
        User, related_name="listas_compartilhadas", blank=True
    )

    nome = models.CharField(max_length=100)
    meta = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    data = models.DateField(default=timezone.now)

    def __str__(self):
        return self.nome.capitalize()

    def save(self, *args, **kwargs):
        if self.nome:
            self.nome = self.nome.capitalize()
        super().save(*args, **kwargs)

    @property
    def total_transacoes(self):
        resultado = self.transacao_set.aggregate(Sum("valor"))
        return resultado["valor__sum"] or 0

    @property
    def diferenca_meta(self):
        return self.meta + self.total_transacoes


class Transacao(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="transacoes"
    )

    categoria = models.ForeignKey(
        Categoria, on_delete=models.SET_NULL, null=True, blank=True
    )

    lista = models.ForeignKey(Lista, on_delete=models.CASCADE, null=True, blank=True)

    valor = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.CharField(max_length=200)
    data = models.DateField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.descricao} (R$ {self.valor})"

    class Meta:
        ordering = ["-data", "-created_at"]
