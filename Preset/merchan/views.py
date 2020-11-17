from django.shortcuts import render
from .models import Merchandise


def merchandise_details(request, product_id: int, merchan_id: int):
    merchan = Merchandise.objects.get(product__id=product_id, id=merchan_id)
    data = {}
    data['merchan'] = merchan
    return render(request, 'merchan/merchandise_details.html', data)
