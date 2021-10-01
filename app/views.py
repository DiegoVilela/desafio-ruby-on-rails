from django.shortcuts import render
from .forms import UploadFileForm
from .models import Transaction, Shop

from datetime import datetime


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


def upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['finance_file']
            for line in uploaded_file:
                parse_line(line)

    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})
