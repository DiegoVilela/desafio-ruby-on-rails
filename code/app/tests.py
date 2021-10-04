from datetime import date, time
from decimal import Decimal

from django.test import TestCase
from django.db.utils import IntegrityError
from django.core.paginator import Page

from finance.settings import BASE_DIR
from .forms import UploadFileForm
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


class ShopViewTest(TestCase):
    """Testa as views de shop"""

    fixtures = ['transactions.json']

    def test_shop_detail_lists_correct_information(self):
        response = self.client.get('/shop/1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop_detail.html', count=1)
        self.assertEqual(len(response.context), 3)

        shop = response.context['shop']
        self.assertTrue(isinstance(shop, Shop))
        self.assertEqual(shop.name, SHOP_NAME)
        self.assertEqual(shop.owner, OWNER)

        page_obj = response.context['page_obj']
        transaction_date = date(2019, 3, 1)
        transaction_cpf = '9620676017'
        self.assertTrue(isinstance(page_obj, Page))
        self.assertEqual(page_obj[0].get_type_display(), 'Financiamento')
        self.assertEqual(page_obj[0].date, transaction_date)
        self.assertEqual(page_obj[0].value, 142.00)
        self.assertEqual(page_obj[0].cpf, transaction_cpf)
        self.assertEqual(page_obj[0].card, '4753****3153')
        self.assertEqual(page_obj[0].time, time(15, 34, 53))

        self.assertEqual(page_obj[1].get_type_display(), 'Débito')
        self.assertEqual(page_obj[1].date, transaction_date)
        self.assertEqual(page_obj[1].value, 152.00)
        self.assertEqual(page_obj[1].cpf, transaction_cpf)
        self.assertEqual(page_obj[1].card, '1234****7890')
        self.assertEqual(page_obj[1].time, time(23, 30, 00))

        self.assertEqual(page_obj[2].get_type_display(), 'Boleto')
        self.assertEqual(page_obj[2].date, transaction_date)
        self.assertEqual(page_obj[2].value, 112.00)
        self.assertEqual(page_obj[2].cpf, transaction_cpf)
        self.assertEqual(page_obj[2].card, '3648****0099')
        self.assertEqual(page_obj[2].time, time(23, 42, 34))

        self.assertEqual(response.context['balance'], -102.00)

        self.assertContains(response, SHOP_NAME, count=2)  # title and h1
        self.assertContains(response, OWNER, count=1)  # h2

    def test_shop_detail_shows_correct_balance(self):
        response = self.client.get('/shop/1')
        self.assertEqual(response.context['balance'], round(Decimal(-102.0), 2))

        response = self.client.get('/shop/3')
        self.assertEqual(response.context['balance'], round(Decimal(489.2), 2))

        response = self.client.get('/shop/5')
        self.assertEqual(response.context['balance'], round(Decimal(152.32), 2))

    def test_status_code_is_404_when_shop_does_not_exist(self):
        response = self.client.get('/shop/6')
        self.assertEqual(response.status_code, 404)


class UploadTest(TestCase):
    """Testa a view upload"""

    def test_form_is_present(self):
        response = self.client.get('/')
        self.assertTrue(isinstance(response.context['form'], UploadFileForm))

    def test_file_upload(self):
        with open(BASE_DIR / 'FINANCEIRO.txt', 'rb') as fp:
            response = self.client.post('/', {'finance_file': fp}, follow=True)
            self.assertEqual(response.status_code, 200)
            page_obj = response.context['page_obj']
            self.assertTrue(isinstance(page_obj, Page))
            self.assertEqual(len(page_obj), 20)
            self.assertTrue('shop' not in response.context)


class ShopAPITest(TestCase):
    """Testa os endpoints do model Shop"""

    fixtures = ['transactions.json']

    def test_getting_shop_list(self):
        response = self.client.get('/api/shops', follow=True)
        self.assertEqual(response.json()['count'], 5)

    def test_getting_one_shop(self):
        response = self.client.get('/api/shops/5', follow=True)
        shop = response.json()
        self.assertEqual(shop['name'], 'LOJA DO Ó - FILIAL')
        self.assertEqual(shop['owner'], 'MARIA JOSEFINA')

    def test_creating_shop(self):
        response = self.client.post(
            '/api/shops/',
            data={'name': 'LOJA 6', 'owner': 'DONO DA LOJA 6'},
            content_type='application/json',
            follow=True,
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(
            response.json(),
            {'id': 6, 'name': 'LOJA 6', 'owner': 'DONO DA LOJA 6'}
        )


class TransactionAPITest(TestCase):
    """Testa os endpoints do model Transaction"""

    fixtures = ['transactions.json']

    def test_getting_shop_list(self):
        response = self.client.get('/api/transactions', follow=True)
        self.assertEqual(response.json()['count'], 21)

    def test_getting_one_shop(self):
        response = self.client.get('/api/transactions/21', follow=True)
        transaction = response.json()
        self.assertEqual(transaction['cpf'], '84515254073')
        self.assertEqual(transaction['value'], '192.00')

    def test_creating_shop(self):
        response = self.client.post(
            '/api/transactions/',
            data={
                'card': '9777****1313',
                'cpf': '74515254073',
                'date': '2021-10-04',
                'shop': 3,
                'time': '17:52:07',
                'type': 3,
                'value': '1.00'},
            content_type='application/json',
            follow=True,
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(
            response.json(),
            {
                'id': 22,
                'card': '9777****1313',
                'cpf': '74515254073',
                'date': '2021-10-04',
                'shop': 3,
                'time': '17:52:07',
                'type': 3,
                'value': '1.00'
            }
        )
