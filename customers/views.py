from rest_framework.generics import (
	ListCreateAPIView,
	RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import AllowAny

from .models import Customer
from .serializers import CustomerSerializer


class CustomerListCreateView(ListCreateAPIView):
	queryset = Customer.objects.all()
	serializer_class = CustomerSerializer
	authentication_classes = []
	permission_classes = [AllowAny]


class CustomerDetailView(RetrieveUpdateDestroyAPIView):
	queryset = Customer.objects.all()
	serializer_class = CustomerSerializer
	authentication_classes = []
	permission_classes = [AllowAny]
