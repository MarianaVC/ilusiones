# api/views.py

from rest_framework import generics
from .serializers import WarehouseSerializer,ProductSerializer,PurchaseOrderCSVSerializer,PurchaseOrderSerializer
from warehouses.models import Warehouse
from products.models import Product
from orders.models import PurchaseOrderCSV,PurchaseOrder

#======== WAREHOUSES ========

class CreateWarehouseView(generics.ListCreateAPIView):
	"""Create behavior of our rest API for model Warehouse."""
	
	queryset = Warehouse.objects.all()
	serializer_class = WarehouseSerializer

	def perform_create(self, serializer):
		"""Save the post data when creating a new warehouse."""
		serializer.save()

class SingleWarehouseView(generics.RetrieveUpdateDestroyAPIView):
	"""Handles http GET, PUT and DELETE requests for a single warehouse."""

	queryset = Warehouse.objects.all()
	serializer_class = WarehouseSerializer

#======== PRODUCTS ========

class CreateProductView(generics.ListCreateAPIView):
	"""Behavior of rest API for model Product"""	
	
	queryset = Product.objects.all()
	serializer_class = ProductSerializer

	def perform_create(self, serializer):
		"""Save the post data when creating a new product."""
		serializer.save()

class SingleProductView(generics.RetrieveUpdateDestroyAPIView):
	"""Handles http GET, PUT and DELETE requests for a single product."""
	
	queryset = Product.objects.all()
	serializer_class = ProductSerializer

#======== PURCHASE ORDER CSV ========

class CreatePurchaseOrderCSVView(generics.ListCreateAPIView):
	"""Create behavior of our rest API for model CSV."""
	queryset = PurchaseOrderCSV.objects.all()
	serializer_class = PurchaseOrderCSVSerializer

	def perform_create(self, serializer):
		serializer.save()

class SinglePurchaseOrderCSVView(generics.RetrieveUpdateDestroyAPIView):
	"""Handles http GET, PUT and DELETE requests for a single csv."""
	
	queryset = PurchaseOrderCSV.objects.all()
	serializer_class = PurchaseOrderCSVSerializer


#======== PURCHASE ORDERS ========

class CreatePurchaseOrderView(generics.ListCreateAPIView):	
	"""Behavior of rest API for model Order"""	
	
	queryset = PurchaseOrder.objects.all()
	serializer_class = PurchaseOrderSerializer

	def perform_create(self, serializer):
		"""Save the post data when creating a new product."""
		serializer.save()

class SinglePurchaseOrderView(generics.RetrieveUpdateDestroyAPIView):		
	"""Handles http GET, PUT and DELETE requests for a single Order."""

	queryset = PurchaseOrder.objects.all()
	serializer_class = PurchaseOrderSerializer
	lookup_field = 'warehouse_id'
