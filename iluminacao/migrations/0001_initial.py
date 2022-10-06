# Generated by Django 3.2.13 on 2022-10-06 18:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bairro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150, verbose_name='Bairro')),
            ],
        ),
        migrations.CreateModel(
            name='Contribuinte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefone', models.CharField(blank=True, max_length=14, verbose_name='Telefone')),
                ('cpf', models.CharField(max_length=14, verbose_name='CPF')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Logradouro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150, verbose_name='Logradouro')),
            ],
        ),
        migrations.CreateModel(
            name='OrdemDeServico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=130)),
                ('motivo_reclamacao', models.CharField(blank=True, max_length=150)),
                ('dt_solicitacao', models.CharField(blank=True, max_length=20, verbose_name='Data de solicitação')),
                ('dt_conclusao', models.CharField(blank=True, max_length=20, verbose_name='Data de conclusão')),
                ('motivo', models.CharField(max_length=150)),
                ('atendente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('contribuinte', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='iluminacao.contribuinte')),
            ],
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referencia', models.CharField(blank=True, max_length=200, verbose_name='Referência')),
                ('bairro', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='iluminacao.bairro', verbose_name='Bairro')),
                ('logradouro', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='iluminacao.logradouro', verbose_name='Logradouro')),
            ],
        ),
    ]