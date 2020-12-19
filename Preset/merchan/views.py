from django.shortcuts import render, redirect
from .models import Merchandise
from .form import MerchanForm
from django.http import Http404, JsonResponse
from django.core.paginator import Paginator


def merchandise_details(request, product_id: int, slug):
    merchan = Merchandise.objects.get(product__id=product_id, slug=slug)
    data = {}
    data['merchan'] = merchan

    data['liked'] = request.user in merchan.likes.all()
    print(merchan.likes.all())

    return render(request, 'merchan/merchan_details.html', data)

def detail(request, slug):
    data = {}
    if not Merchandise.objects.filter(slug=slug).exists():
        raise Http404
    merchan = Merchandise.objects.get(slug=slug)
    data['merchan'] = merchan
    return render(request, 'merchan/detail.html', context=data)

def add_preset(request):
    data = {}
    if request.method == "GET":
        merchan_form = MerchanForm()
        data['merchan_form'] = merchan_form
        return render(request, 'merchan/add_preset.html', context=data)
    elif request.method == "POST":
        merchan_form = MerchanForm(request.POST, request.FILES)
        merchan_form.save()
        return redirect('/product/merchan/merchan_list')

def merchan_list(request):
    data = {}
    all_merchan = Merchandise.objects.all()
    data['merchan'] = all_merchan
    return render(request, 'merchan/merchan_list.html', context=data)



def delete_merchan(request, slug):
    data = {}
    if not request.user.is_authenticated or not Merchandise.objects.filter(slug=slug).exists():
        raise Http404
    merchan = Merchandise.objects.get(slug=slug)
    if request.method == "GET":
        data['merchan'] = merchan
        return render(request, 'merchan/delete_merchan.html', context=data)
    elif request.method == "POST":
        merchan.delete()
        return redirect('/product/merchan/merchan_list')


def update_merchan(request, slug):
    data = {}
    if not request.user.is_authenticated or not Merchandise.objects.filter(slug=slug).exists():
        raise Http404
    merchan = Merchandise.objects.get(slug=slug)
    data['merchan'] = merchan
    if request.method == "GET":
        merchan_form = MerchanForm(instance=merchan)
        data['merchan_form'] = merchan_form
        return render(request, 'merchan/update_merchan.html', context=data)
    elif request.method == "POST":
        merchan_form = MerchanForm(request.POST)
        if merchan_form.is_valid():
            merchan.name = merchan_form.cleaned_data['name']
            merchan.about_preset = merchan_form.cleaned_data['about_preset']
            merchan.product = merchan_form.cleaned_data['product']
            merchan.before_img = merchan_form.cleaned_data['before_img']
            merchan.after_img = merchan_form.cleaned_data['after_img']
            merchan.cost = merchan_form.cleaned_data['cost']
            merchan.save()
        else:
            print('NOT VALID FORM!')
        return redirect('/product/merchan/merchan_list')


def ajax_like(request, slug):
    response = dict()
    response['status'] = 'error'
    if request.user.is_authenticated:
        if not Merchandise.objects.filter(slug=slug).exists():
            raise Http404
        merchan = Merchandise.objects.get(slug=slug)
        like_action = request.GET.get('like_action')
        if like_action == 'add':
            merchan.likes.add(request.user)
            response['status'] = 'ok'
        elif like_action == 'remove':
            merchan.likes.remove(request.user)
            response['status'] = 'ok'
    return JsonResponse(response)
