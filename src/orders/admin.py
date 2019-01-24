from django.contrib import admin
from .models import PurchaseOrderCVS, PurchaseOrder

# Register your models here.

class PurchaseOrderInline(admin.TabularInline):
	model = PurchaseOrder
	extra = 1
	max_num = 400
	fields = ('purchase_order','product','quantity','warehouse','ready','created_at','updated_at')
	readonly_fields = ('purchase_order','created_at','updated_at')


class PurchaseOrderCVSAdmin(admin.ModelAdmin):
	"""Model admin for Warehouse"""
	fields = ('file','created_at','updated_at','author')
	readonly_fields = ('created_at','updated_at','author')
	list_display = ('file','created_at','updated_at','author')
	list_filter = ('created_at','updated_at','author','file')
	search_fields = ['file']
	inlines = [PurchaseOrderInline]




admin.site.register(PurchaseOrderCVS, PurchaseOrderCVSAdmin)
