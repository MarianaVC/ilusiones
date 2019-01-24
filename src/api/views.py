# api/views.py

from rest_framework import generics
from .serializers import WarehouseSerializer
from warehouses.models import Warehouse


class CreateWarehouseView(generics.ListCreateAPIView):
    """Create behavior of our rest api for model Warehouse."""
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new warehouse."""
        serializer.save()

class SingleWarehouseView(generics.RetrieveUpdateDestroyAPIView):
    """Handles http GET, PUT and DELETE requests for a single warehouse."""

    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer