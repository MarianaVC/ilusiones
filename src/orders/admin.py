from django.contrib import admin
from .models import PurchaseOrderCSV, PurchaseOrder
from django.core.urlresolvers import reverse
from django.utils.html import format_html
from django.utils.safestring import mark_safe

# Register your models here.

class PurchaseOrderInline(admin.TabularInline):
	model = PurchaseOrder
	extra = 1
	max_num = 400
	fields = ('purchase_order','product','quantity','warehouse','ready','created_at','updated_at')
	readonly_fields = ('purchase_order','created_at','updated_at')


class PurchaseOrderCSVAdmin(admin.ModelAdmin):
	"""Model admin for Warehouse"""
	fields = ('file','fieldname_download','created_at','updated_at','author')
	readonly_fields = ('created_at','updated_at','author','fieldname_download')
	list_display = ('link_to_csv','fieldname_download','created_at','updated_at','author')
	list_filter = ('created_at','updated_at','author','file')
	search_fields = ['file']
	inlines = [PurchaseOrderInline]

	def link_to_csv(self, obj):
		link = reverse("admin:orders_purchaseordercsv_change", args=[obj.id])
		return format_html('<a href="{}"> Detalle</a>', link)

	def fieldname_download(self,obj):
		return mark_safe('<a href="/media/documents" download>{0}</a>'.format(
			obj.file))
	
	link_to_csv.short_description = 'Go to csv detail'
	fieldname_download.short_description = 'Download Fieldname'


admin.site.register(PurchaseOrderCSV, PurchaseOrderCSVAdmin)
