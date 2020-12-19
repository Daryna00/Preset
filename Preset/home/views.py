from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import ContactForm
from merchan.models import Merchandise
from product.models import Product
from .models import Order
from django.core.paginator import Paginator
from django.db.models import Q
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import get_template
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, JsonResponse

def contact(request):
    data = {}
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form_email = form.cleaned_data.get('from_email')
        form_subject = form.cleaned_data.get('subject')
        form_text = form.cleaned_data.get('message')
        header = 'Website: My Preset!'
        email_admin = settings.DEFAULT_TO_EMAIL
        text = f"""
            
            {form_email} 
            {form_subject} 
            

            Message:
                {form_text}
            """
        html_file = get_template('home/mail.html')

        data['form_text'] = form_text
        data['form_subject'] = form_subject
        data['form_email'] = form_email
        html_content = html_file.render(context=data)

        send_mail(header, text, email_admin, [email_admin, '@gmail.com'], fail_silently=False, html_message=html_content)
    data['form'] = form
    return render(request, 'home/contact.html', context=data)

# Create your views here.
def index(request):
    data = dict()
    product = Product.objects.all()

    filtered_product = request.GET.getlist('product')
    filtered_product = list(map(int, filtered_product))
    if request.user.is_authenticated:
        all_orders = Order.objects.filter()
        data['orders'] = all_orders
    if filtered_product:
        merchan = Merchandise.objects.filter(product__id__in=filtered_product)
    else:
        merchan = Merchandise.objects.all()

    paginator = Paginator(product, 6)
    page1_number = request.GET.get('page1')
    page1_obj = paginator.get_page(page1_number)
    data['page1_obj'] = page1_obj

    search = request.GET.get('search')
    if search:
        result_posts = merchan.filter(
            Q(name__icontains=search)
        )
        merchan = result_posts
        data['search'] = search

    paginator = Paginator(merchan, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    data['page_obj'] = page_obj
    data['product'] = product
    data['merchan'] = merchan

    return render(request, 'home/index.html', context=data)


def what_is_it(request):
    return render(request, 'home/what-is-it.html')


def sign_in(request):
    data = {}
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect("/mypage")
        return render(request, 'home/login.html', context=data)
    elif request.method == "POST":
        data2 = {}

        _login = request.POST.get('login_field')
        _password = request.POST.get('password_field')

        user = authenticate(request, username=_login, password=_password)
        if user is None:
            data['report'] = 'Пользователь не найден или неверный пароль!'
            return render(request, 'home/login.html', context=data2)
        else:
            login(request, user)
            return redirect("/mypage")


def logout_user(request):
    logout(request)
    return redirect("/")


def register(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect("/mypage")
        return render(request, 'home/register.html')
    elif request.method == "POST":
        login = request.POST.get('login_field')
        email = request.POST.get('email_field')
        pass1 = request.POST.get('password_field')
        pass2 = request.POST.get('password_confirm_field')

        data = dict()
        data['login'] = login
        data['email'] = email
        data['pass1'] = pass1
        data['pass2'] = pass2

        if pass1 != pass2:
            report = 'Пароли должны совпадать'
        elif '' in data.values():
            report = 'Все поля - ОБЯЗАТЕЛЬНЫЕ'
        elif len(pass1) < 8:
            report = 'Слишком короткий пароль'
        else:
            user = User.objects.create_user(login, email, pass1)
            user.save()
            if user:
                return redirect("/mypage")
            report = 'Что-то страшное произошло!'
        data['report'] = report
        return render(request, 'home/register.html', context=data)


def my_page(request):
    data = {}
    return render(request, 'home/login-page.html', context=data)

def ajax_reg_login(request) -> JsonResponse:
    response = dict()
    _login = request.GET.get('login_field')

    try:
        User.objects.get(username=_login)
        response['message_login'] = "занят"
    except User.DoesNotExist:
        response['message_login'] = "свободен"

    return JsonResponse(response)


def add_to_card(request, slug):
    if not request.user.is_authenticated:
        return redirect('/')

    try:
        merchan = Merchandise.objects.get(slug=slug)
        new_order = Order(customer=request.user, merchan=merchan, count=0)
        my_orders_with_merchan = Order.objects.filter(customer=request.user, merchan=merchan)
        if my_orders_with_merchan.exists():
            new_order = my_orders_with_merchan.first()
        new_order.count += 1
        new_order.save()
        print(new_order)
        return redirect('homepage')
    except ObjectDoesNotExist:
        raise Http404

def delete_from_card(request, slug):
    result = {}
    result['status'] = 'error'

    if not request.user.is_authenticated:
        return JsonResponse(result)

    try:
        merchan = Merchandise.objects.get(slug=slug)
        order = Order.objects.get(customer=request.user, merchan=merchan)
        order.delete()
        result['status'] = 'ok'
        return JsonResponse(result)
    except ObjectDoesNotExist:
        return JsonResponse(result)


def change_order_count(request, order_id):
    result = {}
    result['status'] = 'error'
    if request.user.is_authenticated:
        if Order.objects.filter(id=order_id, customer=request.user).exists():
            order = Order.objects.get(id=order_id, customer=request.user)
            action = request.GET.get('action')
            current_order_number = order.count
            print(current_order_number)
            if action == 'increase':
                current_order_number += 1
            elif action == 'decrease' and current_order_number > 1:
                current_order_number -= 1

            order.count = current_order_number
            order.save()

            result['status'] = 'ok'
            result['new_number'] = current_order_number
    return JsonResponse(result)
