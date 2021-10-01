from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .forms import UploadFileForm
from .models import Transaction, Shop

from datetime import datetime


SUBTRACTION_TRANSACTION_TYPES = [2, 3, 9]


def parse_line(line):
    line = line.decode('utf8')

    shop_name = line[62:81].strip()
    shop = Shop.objects.get_or_create(
        name=shop_name,
        owner=line[48:62].strip(),
    )

    Transaction.objects.create(
        type=int(line[0:1]),
        date=datetime.strptime(line[1:9], '%Y%m%d').date(),
        value=int(line[9:19]),
        cpf=int(line[19:30]),
        card=line[30:42],
        time=datetime.strptime(line[42:48], '%H%M%S').time(),
        shop=shop[0],
    )


def get_page(number):
    transactions = Transaction.objects.all()
    paginator = Paginator(transactions, 20)
    return paginator.get_page(number)


def upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['finance_file']
            for line in uploaded_file:
                parse_line(line)
    else:
        form = UploadFileForm()

    return render(request, 'upload.html', {
        'form': form,
        'page_obj': get_page(request.GET.get('page')),
    })


def shop_detail(request, shop_id):
    shop = get_object_or_404(Shop, pk=shop_id)
    transactions = Transaction.objects.filter(shop=shop)
    balance = 0
    for transaction in transactions:
        if transaction.type in SUBTRACTION_TRANSACTION_TYPES:
            balance -= transaction.value
        else:
            balance += transaction.value
    paginator = Paginator(transactions, 20)

    return render(request, 'shop_detail.html', {
        'shop': shop,
        'page_obj': paginator.get_page(request.GET.get('page')),
        'balance': balance,
    })
