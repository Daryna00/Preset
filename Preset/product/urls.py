from django.urls import path, include
from .views import index, create_product, delete_product, update_product, product_detail, product_list

urlpatterns = [
    path('', index, name='product_homepage'),
    path('create', create_product, name='create_product'),
    path('<int:id>/delete', delete_product, name='delete_product'),
    path('<int:id>/update', update_product, name='update_product'),
    path('<int:id>/details', product_detail, name='product_detail'),
    path('list', product_list, name='product_list'),
    path('', include('merchan.urls'))
]
