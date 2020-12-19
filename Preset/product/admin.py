from django.contrib import admin
from .models import Product

# Register your models here.
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'timestamp', 'updated', 'draft']
    list_display_links = ['timestamp']
    list_editable = ['name']

    list_filter = ['name', 'timestamp', 'updated']
    search_fields = ['name']

    class Meta:
        model = Product

admin.site.register(Product, ProductModelAdmin)
