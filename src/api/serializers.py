# api/serializers.py
from rest_framework import serializers
from warehouses.models import Warehouse

class WarehouseSerializer(serializers.ModelSerializer):
	"""Serializer to map the Model instance into JSON format."""
	
	class Meta:
		"""Meta class to map serializer's fields with the model fields."""
		model = Warehouse
		fields = ('pdv','sub_inventory_id','created_at','updated_at','author')
		read_only_fields = ('created_at', 'updated_at','author')
