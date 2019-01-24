from django.db import models
from datetime import date
from django.contrib.auth.models import User
from django.utils import timezone


class Warehouse(models.Model):
	"""Warehouses model"""
	pdv = models.CharField('PDV', blank = False, null = False, max_length = 400)
	sub_inventory_id = models.CharField('Sub-inventory Id', blank = False, null = False, unique = True ,max_length = 250)
	created_at = models.DateTimeField('Created at',auto_now_add=True)
	updated_at = models.DateTimeField('Updated at',auto_now=True, blank = True, null = True)
	author = models.ForeignKey(User,verbose_name = 'Created by',related_name = 'warehouse_author' ,on_delete = models.DO_NOTHING, blank = True, null=True)

	def __str__(self):
		"""Model object representation"""
		return self.pdv

	def save(self, *args, **kwargs):
		"""Update created_at or updated_at fields depending on pk"""
		if not self.id:
			# Newly created object, so set created_at
			self.created_at = timezone.now()
		else:
			self.updated_at = timezone.now()

		super(Warehouse, self).save(*args, **kwargs)


	class Meta:
		verbose_name = 'Warehouse'
		verbose_name_plural = "Warehousees"

