from django.shortcuts import render, redirect
from .models import Product
from .form import ProductForm


def index(request):
    return render(request, 'product/index.html')


def create_product(request):
    data = {}
    if request.method == "GET":
        group_form = ProductForm()
        data['group_form'] = group_form
        return render(request, 'product/create.html', context=data)
    elif request.method == "POST":
        group_form = ProductForm(request.POST)
        group_form.save()
        return redirect('/product/list')




def delete_product(request, id: int):
    return render(request, 'product/delete.html')


def product_detail(request, id: int):
    return render(request, 'product/details.html')


def product_list(request):
    data = {}
    all_product = Product.objects.all()

    data['product'] = all_product
    return render(request, 'product/list.html', context=data)


def update_product(request, id: int):
    return render(request, 'product/update.html')