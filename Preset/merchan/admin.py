from django.contrib import admin
from .models import Merchandise

# Register your models here.
class MerchandiseModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'timestamp', 'updated', 'draft']
    list_display_links = ['timestamp']
    list_editable = ['name']

    list_filter = ['name', 'timestamp', 'updated']
    search_fields = ['name']

    class Meta:
        model = Merchandise
admin.site.register(Merchandise, MerchandiseModelAdmin)