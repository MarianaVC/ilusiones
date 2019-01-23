from django.db import models
from datetime import date
from django.contrib.auth.models import User


class Warehouse(models.Model):
	"""Warehouses model"""
	pdv = models.CharField('PDV', blank = False, null = False, max_length = 400)
	sub_inventory_id = models.CharField('Sub-inventory Id', blank = False, null = False, unique = True ,max_length = 250)
	created_at = models.DateTimeField('Created at',auto_now_add=True)
	updated_at = models.DateTimeField('Updated at', blank = True, null = False)
	author = models.ForeignKey(User,verbose_name = 'Created by',related_name = 'warehouse_author' ,on_delete = models.DO_NOTHING)

	def __str__(self):
		"""Model object representation"""
		return self.pdv

	class Meta:
		verbose_name = 'Warehouse'
		verbose_name_plural = "Warehousees"

