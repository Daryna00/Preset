from django.urls import path, include
from .views import index, what_is_it, sign_in, register, logout_user, my_page, ajax_reg_login, contact, change_order_count, delete_from_card, add_to_card


urlpatterns = [
    path('', index, name='homepage'),
    path('what_is_it', what_is_it, name='what_is_it'),
    path('login', sign_in, name='login-page'),
    path('register', register, name='register'),
    path('logout', logout_user, name='logout'),
    path('mypage', my_page, name='mypage'),
    path('/contact', contact, name='contact'),
    path('ajax_reg_login', ajax_reg_login, name='ajax_reg_login'),
    path('change_order_count/<int:order_id>', change_order_count, name='change_order_count'),
    path('add_to_cart/<slug:slug>', add_to_card, name='add_to_card'),
    path('delete_from_card/<slug:slug>', delete_from_card, name='delete_from_card'),
    path('', include('merchan.urls')),
    ]
