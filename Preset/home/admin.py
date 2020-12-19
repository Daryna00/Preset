from django.contrib import admin
from django.urls import path, include
from .models import Order

# Register your models here.
admin.site.register(Order)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
]