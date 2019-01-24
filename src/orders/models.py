from django.db import models
from warehouses.models import Warehouse
from products.models import Product
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class PurchaseOrderCVS(models.Model):
	"""Definition for model Purchase Order CVS"""
	created_at = models.DateTimeField('Created at',auto_now_add = True)
	updated_at = models.DateTimeField('Updated at',auto_now = True,blank = True, null = True) 
	author = models.ForeignKey(User,verbose_name = 'Created by',on_delete = models.DO_NOTHING, related_name = 'purchaseorder_author', blank = True, null = True)
	file = models.FileField('File',blank = False, null = False)
	
	class Meta:
		verbose_name = 'CSV de Orden de compra'
		verbose_name_plural = 'CSVs de Órdenes de compra'
		unique_together = ['created_at', 'file']

class PurchaseOrder(models.Model):
	"""Definition for model purchase order this is unique for each warehouse and each csv"""
	purchase_order = models.ForeignKey(PurchaseOrderCVS, related_name = 'order')
	product = models.ForeignKey(Product, related_name = 'order_product')	
	quantity = models.PositiveIntegerField(default = 0, blank = False, null = False)
	warehouse = models.ForeignKey(Warehouse, related_name = 'order_warehouse')
	ready = models.BooleanField(default = True)
	created_at = models.DateTimeField('Created at',auto_now_add = True)
	updated_at = models.DateTimeField('Updated at',auto_now = True,blank = True, null = True) 

	class Meta:
		verbose_name = 'Orden de compra'
		verbose_name_plural = 'Órdenes de compra'
		unique_together = ['purchase_order','warehouse','product']