from django.contrib import admin
from .models import Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
	"""Model admin for Product"""
	fields = ('imei','sku','created_at','updated_at','author')
	readonly_fields = ('created_at','updated_at','author')
	list_display = ('imei','sku','created_at','updated_at','author')
	list_filter = ('created_at','updated_at','author')
	search_fields = ('imei','sku','author')

admin.site.register(Product, ProductAdmin)

# Register your models here.

