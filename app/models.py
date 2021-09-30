from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Shop(models.Model):
    """Representa uma loja"""

    name = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)


class Transaction(models.Model):
    """Representa um registro financeiro."""

    TYPE = (
        (1, 'Débito'),
        (2, 'Boleto'),
        (3, 'Financiamento'),
        (4, 'Crédito'),
        (5, 'Recebimento Empréstimo'),
        (6, 'Vebdas'),
        (7, 'Recebimento TED'),
        (8, 'Recebimento DOC'),
        (9, 'Aluguel'),
    )
    type = models.PositiveSmallIntegerField(
        choices=TYPE,
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(9)],
    )
    date = models.DateField()
    value = models.IntegerField()
    cpf = models.IntegerField()
    time = models.TimeField()
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)

