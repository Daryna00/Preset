from django.shortcuts import render, redirect
from .models import Product
from .form import ProductForm
from django.http import Http404
from merchan.models import Merchandise


def index(request):
    return render(request, 'product/index.html')


def create_product(request):
    data = {}
    if request.method == "GET":
        group_form = ProductForm()
        data['group_form'] = group_form
        return render(request, 'product/create.html', context=data)
    elif request.method == "POST":
        group_form = ProductForm(request.POST, request.FILES)
        group_form.save()
        return redirect('/product/list')



def delete_product(request, slug):
    data = {}
    if not request.user.is_authenticated or not Product.objects.filter(slug=slug).exists():
        raise Http404
    product = Product.objects.get(slug=slug)
    if request.method == "GET":
        data['product'] = product
        return render(request, 'product/delete.html', context=data)
    elif request.method == "POST":
        product.delete()
        return redirect('/product/list')


def product_detail(request, slug):
    data = {}
    if not Product.objects.filter(slug=slug).exists():
        raise Http404
    product = Product.objects.get(slug=slug)

    # Секция со студентами
    data['product'] = product
    merchan = Merchandise.objects.filter(product__id=product.id)
    data['merchan'] = merchan
    return render(request, 'product/details.html', context=data)


def product_list(request):
    data = {}
    all_product = Product.objects.all()
    data['product'] = all_product
    return render(request, 'product/list.html', context=data)


def update_product(request, slug):
    data = {}
    if not request.user.is_authenticated or not Product.objects.filter(slug=slug).exists():
        raise Http404
    product = Product.objects.get(slug=slug)
    data['product'] = product
    if request.method == "GET":
        product_form = ProductForm(instance=product)
        data['product_form'] = product_form
        return render(request, 'product/update.html', context=data)
    elif request.method == "POST":
        product_form = ProductForm(request.POST)
        if product_form.is_valid():
            product.image = product_form.cleaned_data['image']
            product.name = product_form.cleaned_data['name']
            product.about = product_form.cleaned_data['about']
            product.max_presets = product_form.cleaned_data['max_presets']
            product.is_discount_preset = product_form.cleaned_data['is_discount_preset']
            product.save()
        else:
            print('NOT VALID FORM!')

        return redirect('/product/list')