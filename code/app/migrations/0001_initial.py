# Generated by Django 3.2.7 on 2021-10-04 22:41

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('owner', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.PositiveSmallIntegerField(choices=[(1, 'Débito'), (2, 'Boleto'), (3, 'Financiamento'), (4, 'Crédito'), (5, 'Recebimento Empréstimo'), (6, 'Vendas'), (7, 'Recebimento TED'), (8, 'Recebimento DOC'), (9, 'Aluguel')], default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(9)])),
                ('date', models.DateField()),
                ('value', models.DecimalField(decimal_places=2, max_digits=6)),
                ('cpf', models.CharField(max_length=11)),
                ('card', models.CharField(max_length=12)),
                ('time', models.TimeField()),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.shop')),
            ],
            options={
                'ordering': ['date', 'time'],
            },
        ),
    ]