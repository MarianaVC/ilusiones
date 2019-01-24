from django.db import models
from warehouses.models import Warehouse
from products.models import Product
from django.contrib.auth.models import User
from django.utils import timezone
from .validators import validate_file_extension
# Create your models here.

class PurchaseOrderCSV(models.Model):
	"""Definition for model Purchase Order CSV"""
	created_at = models.DateTimeField('Created at',auto_now_add = True)
	updated_at = models.DateTimeField('Updated at',auto_now = True,blank = True, null = True) 
	author = models.ForeignKey(User,verbose_name = 'Created by',on_delete = models.DO_NOTHING, related_name = 'purchaseorder_author', blank = True, null = True)
	file = models.FileField('File',blank = False, upload_to = 'documents/' ,null = False,validators=[validate_file_extension])
	
	def __str__(self):
		"""Model object representation"""
		return str(self.created_at)

	def save(self, *args, **kwargs):
		"""Update created_at or updated_at fields depending on pk"""
		if not self.id:
			# Newly created object, so set created_at
			self.created_at = timezone.now()
		else:
			self.updated_at = timezone.now()

		super(PurchaseOrderCSV, self).save(*args, **kwargs)



	class Meta:
		verbose_name = 'CSV de Orden de compra'
		verbose_name_plural = 'CSVs de Órdenes de compra'
		unique_together = ['created_at', 'file']

class PurchaseOrder(models.Model):
	"""Definition for model purchase order this is unique for each warehouse and each csv"""
	purchase_order = models.ForeignKey(PurchaseOrderCSV, related_name = 'order')
	product = models.ForeignKey(Product, related_name = 'order_product')	
	quantity = models.PositiveIntegerField(default = 0, blank = False, null = False)
	warehouse = models.ForeignKey(Warehouse, related_name = 'order_warehouse')
	ready = models.BooleanField(default = True)
	created_at = models.DateTimeField('Created at',auto_now_add = True)
	updated_at = models.DateTimeField('Updated at',auto_now = True,blank = True, null = True) 

	def __str__(self):
		"""Model object representation"""
		return self.warehouse

	def save(self, *args, **kwargs):
		"""Update created_at or updated_at fields depending on pk"""
		if not self.id:
			# Newly created object, so set created_at
			self.created_at = timezone.now()
		else:
			self.updated_at = timezone.now()

		super(PurchaseOrder, self).save(*args, **kwargs)

	class Meta:
		verbose_name = 'Orden de compra'
		verbose_name_plural = 'Órdenes de compra'
		unique_together = ['purchase_order','warehouse','product']