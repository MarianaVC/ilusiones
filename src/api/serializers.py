# api/serializers.py
from rest_framework import serializers
from warehouses.models import Warehouse
from products.models import Product
from orders.models import PurchaseOrderCSV,PurchaseOrder

class WarehouseSerializer(serializers.ModelSerializer):
	"""Serializer to map the Model Warehouse instance into JSON format."""
	
	class Meta:
		"""Meta class to map serializer's fields with the model fields."""
		model = Warehouse
		fields = ('pdv','sub_inventory_id','created_at','updated_at','author')
		read_only_fields = ('created_at', 'updated_at','author')

class ProductSerializer(serializers.ModelSerializer):
	"""Serializer to map the Model Product instance into JSON format."""

	class Meta:
		"""Meta class to map serializer's fields with model fields"""
		model = Product
		fields = ('imei','sku','created_at', 'updated_at', 'author')
		read_only_fields = ('created_at', 'updated_at', 'author')

class PurchaseOrderCSVSerializer(serializers.ModelSerializer):
	"""Serializer to map the Model 	CSV instance into JSON format."""

	class Meta:
		"""Meta class to map serializer's fields with the model fields."""
		model = PurchaseOrderCSV
		fields = ('created_at','updated_at','author','file')
		read_only_fields = ('created_at','updated_at','author')

class PurchaseOrderSerializer(serializers.ModelSerializer):
	"""Serializer to map the Model Order instance into JSON format."""

	class Meta:
		"""Meta class to map serializer's fields with the model fields."""
		model = PurchaseOrder
		fields = ('purchase_order','product','quantity','warehouse','ready','created_at','updated_at')
		read_only_fields = ('created_at','updated_at')		



