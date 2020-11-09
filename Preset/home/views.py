from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    return render(request, 'home/index.html')


def what_is_it(request):
    return render(request, 'home/what-is-it.html')


def sign_in(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect("/mypage")
        return render(request, 'home/login.html')
    elif request.method == "POST":
        data = {}

        _login = request.POST.get('login_field')
        _password = request.POST.get('password_field')

        user = authenticate(request, username=_login, password=_password)
        if user is None:
            data['report'] = 'Пользователь не найден или неверный пароль!'
            return render(request, 'home/login.html', context=data)
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
        return render(request, 'home/register.html', context={})
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
    return render(request, 'home/login-page.html')