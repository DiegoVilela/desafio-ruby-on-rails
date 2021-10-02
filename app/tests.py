from django.test import TestCase
from django.shortcuts import reverse
from django.db.utils import IntegrityError

from .models import Shop, Transaction


SHOP_NAME = 'BAR DO JOÃO'
OWNER = 'JOÃO MACEDO'


class ShopTest(TestCase):
    """Testa o model Shop"""

    fixtures = ['transactions.json']

    def test_shop_as_string_returns_shop_and_owner_names(self):
        shop = Shop.objects.get(pk=1)
        self.assertEqual(str(shop), f'{SHOP_NAME} Dono: {OWNER}')

    def test_duplicate_name_raises_exception(self):
        with self.assertRaises(IntegrityError):
            Shop.objects.create(name=SHOP_NAME, owner=OWNER)

    def test_absolute_url_returns_correct_path(self):
        shop = Shop.objects.get(pk=1)
        self.assertEqual(shop.get_absolute_url(), '/shop/1')


class TransactionTest(TestCase):
    """Testa o model Transaction"""

    fixtures = ['transactions.json']

    def test_transaction_as_string_returns_correct_string(self):
        t = Transaction.objects.get(pk=1)
        self.assertEqual(str(t), f'{t.get_type_display()} {t.date} {t.time} {t.cpf}')

