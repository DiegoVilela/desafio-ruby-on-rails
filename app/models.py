from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse


class Shop(models.Model):
    """Representa uma loja"""

    name = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} Dono: {self.owner}'

    def get_absolute_url(self):
        return reverse('shop_detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['name']


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
    card = models.CharField(max_length=12)
    time = models.TimeField()
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.get_type_display()} {self.date} {self.time} {self.cpf}'
