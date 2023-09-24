# Generated by Django 4.2.5 on 2023-09-23 22:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cria_lista', '0020_lista_user_alter_item_lista_alter_lista_categoria_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lista',
            name='categoria',
            field=models.CharField(choices=[('Compras-do-mes', 'Compras do mês'), ('Transporte', 'Transporte'), ('Lazer', 'Lazer'), ('Alimentacao-fora', 'Alimentação fora de casa'), ('Outros', 'Outros')], max_length=50),
        ),
        migrations.AlterField(
            model_name='lista',
            name='tipo',
            field=models.CharField(choices=[('Prioritários', 'Prioritários'), ('Secundários', 'Secundários'), ('Luxo', 'Luxo'), ('Outros', 'Outros')], max_length=50),
        ),
        migrations.AlterField(
            model_name='lista',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
