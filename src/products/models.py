from django.db import models
from datetime import date
from warehouses.models import Warehouse
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
	"""Product model"""
	imei = models.CharField('IMEI', blank = False, null = False, max_length = 400, unique = True) 
	sku = models.CharField('SKU', blank = False, null = False, max_length = 400, unique = True) 
	created_at = models.DateTimeField('Created at',auto_now_add = True)
	updated_at = models.DateTimeField('Updated at', blank = True, null = False)
	author = models.ForeignKey(User,verbose_name = 'Created by',on_delete = models.DO_NOTHING, related_name = 'product_author')

	def __str__(self):
		"""Model object representation"""
		return self.sku

	class Meta:
		verbose_name = 'Producto'
		verbose_name_plural = "Productos"

class Stock(models.Model):
	"""Stock model for Warehouses"""
	product = models.ForeignKey(Product, on_delete = models.CASCADE, related_name = 'stock_product')
	warehouse = models.ForeignKey(Warehouse, on_delete = models.DO_NOTHING, related_name = 'stock_warehouse')
	quantity = models.PositiveIntegerField('Quantity', default = 0, null = False, blank = False)
	author = models.ForeignKey(User,verbose_name = 'Created by',on_delete = models.DO_NOTHING, related_name = 'stock_author')
	created_at = models.DateTimeField('Created at',auto_now_add = True)
	updated_at = models.DateTimeField('Updated at', blank = True, null = False) 
	
	class Meta:
		verbose_name = 'Stock de almacen'
		verbose_name_plural = 'Stock de almacenes'

