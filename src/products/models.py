from django.db import models
from datetime import date
from warehouses.models import Warehouse
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Product(models.Model):
	"""Product model"""
	imei = models.CharField('IMEI', blank = False, null = False, max_length = 400, unique = True) 
	sku = models.CharField('SKU', blank = False, null = False, max_length = 400, unique = True) 
	created_at = models.DateTimeField('Created at',auto_now_add = True)
	updated_at = models.DateTimeField('Updated at', auto_now = True ,blank = True, null = True)
	author = models.ForeignKey(User,verbose_name = 'Created by',on_delete = models.DO_NOTHING, related_name = 'product_author', blank = True, null = True)

	def __str__(self):
		"""Model object representation"""
		return self.sku

	def save(self, *args, **kwargs):
		"""Update created_at or updated_at fields depending on pk"""
		if not self.id:
			# Newly created object, so set created_at
			self.created_at = timezone.now()
		else:
			self.updated_at = timezone.now()

		super(Product, self).save(*args, **kwargs)

	class Meta:
		verbose_name = 'Producto'
		verbose_name_plural = "Productos"

class Stock(models.Model):
	"""Stock model for Warehouses"""
	product = models.ForeignKey(Product, on_delete = models.CASCADE, related_name = 'stock_product')
	warehouse = models.ForeignKey(Warehouse, on_delete = models.DO_NOTHING, related_name = 'stock_warehouse')
	quantity = models.PositiveIntegerField('Quantity', default = 0, null = False, blank = False)
	author = models.ForeignKey(User,verbose_name = 'Created by',on_delete = models.DO_NOTHING, related_name = 'stock_author', blank = True, null = True)
	created_at = models.DateTimeField('Created at',auto_now_add = True)
	updated_at = models.DateTimeField('Updated at',auto_now = True,blank = True, null = True) 
	
	def save(self, *args, **kwargs):
		"""Update created_at or updated_at fields depending on pk"""
		if not self.id:
			# Newly created object, so set created_at
			self.created_at = timezone.now()
		else:
			self.updated_at = timezone.now()

		super(Stock, self).save(*args, **kwargs)

	class Meta:
		verbose_name = 'Stock de almacen'
		verbose_name_plural = 'Stock de almacenes'

