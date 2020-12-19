from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import index, create_product, delete_product, update_product, product_detail, product_list

urlpatterns = [
    path('', index, name='product_homepage'),
    path('create', create_product, name='create_product'),
    path('<slug:slug>/delete', delete_product, name='delete_product'),
    path('<slug:slug>/update', update_product, name='update_product'),
    path('<slug:slug>/details', product_detail, name='product_detail'),
    path('list', product_list, name='product_list'),
    path('', include('merchan.urls'))

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
