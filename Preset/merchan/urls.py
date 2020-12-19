from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import merchandise_details, add_preset, merchan_list, delete_merchan, update_merchan, detail, ajax_like

urlpatterns = [
    path('<int:product_id>/merchan/<slug:slug>', merchandise_details, name='merchan_details'),
    path('merchan/add_preset', add_preset, name='add_preset'),
    path('merchan/merchan_list', merchan_list, name='merchan_list'),
    path('merchan/<slug:slug>/delete_merchan', delete_merchan, name='delete_merchan'),
    path('merchan/<slug:slug>/update_merchan', update_merchan, name='update_merchan'),
    path('merchan/<slug:slug>/detail', detail, name='detail'),
    path('merchan/<slug:slug>/like', ajax_like, name='ajax_like'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
