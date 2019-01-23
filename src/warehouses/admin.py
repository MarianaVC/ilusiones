from django.contrib import admin
from .models import Warehouse
# Register your models here.

class WarehouseAdmin(admin.ModelAdmin):
	"""Model admin for Warehouse"""
	fields = ('pdv','sub_inventory_id','created_at','updated_at','author')
	readonly_fields = ('created_at','updated_at','author')
	list_display = ('pdv','sub_inventory_id','created_at','author')
	list_filter = ('created_at','updated_at','author')
	search_fields = ('pdv','sub_inventory_id')

admin.site.register(Warehouse, WarehouseAdmin)
