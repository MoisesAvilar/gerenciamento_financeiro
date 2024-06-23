from django.contrib import admin
from earning.models import Earning


@admin.register(Earning)
class EarningAdmin(admin.ModelAdmin):
    list_display = ('earning', 'category')
