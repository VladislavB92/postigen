from rest_framework.generics import (
	ListCreateAPIView,
	RetrieveUpdateDestroyAPIView,
)
from .models import Customer
from .serializers import CustomerSerializer


class CustomerListCreateView(ListCreateAPIView):
	queryset = Customer.objects.all()
	serializer_class = CustomerSerializer


class CustomerDetailView(RetrieveUpdateDestroyAPIView):
	queryset = Customer.objects.all()
	serializer_class = CustomerSerializer
