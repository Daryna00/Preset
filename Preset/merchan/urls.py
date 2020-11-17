from django.urls import path
from .views import merchandise_details

urlpatterns = [
    path('<int:product_id>/merchan/<int:merchan_id>', merchandise_details, name='merchan_details'),
]