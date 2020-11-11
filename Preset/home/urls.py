from django.urls import path
from .views import index, what_is_it, sign_in, register, logout_user, my_page, ajax_reg


urlpatterns = [
    path('', index, name='homepage'),
    path('what_is_it', what_is_it, name='what_is_it'),
    path('login', sign_in, name='login-page'),
    path('register', register, name='register'),
    path('logout', logout_user, name='logout'),
    path('mypage', my_page, name='mypage'),
    path('ajax_reg', ajax_reg, name='ajax_reg')
]