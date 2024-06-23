from django.db import models
from django.contrib.auth.models import User


CATEGORY = (
    ('RENDA_EXTRA', 'Renda extra'),
    ('ALUGUEL', 'Aluguel'),
    ('DIVIDENDOS', 'Dividendos'),
    ('OUTROS', 'Outros'),
)


class Earning(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    earning = models.FloatField(null=False, blank=False)
    category = models.CharField(max_length=50, choices=CATEGORY, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_category_display(self):
        return dict(CATEGORY).get(self.category, self.category)
