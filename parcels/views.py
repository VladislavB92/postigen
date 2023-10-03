from rest_framework.generics import (
	ListCreateAPIView,
	RetrieveUpdateDestroyAPIView,
)
from .models import Parcel
from .serializers import ParcelSerializer


class ParcelListCreateView(ListCreateAPIView):
	queryset = Parcel.objects.all()
	serializer_class = ParcelSerializer


class ParcelDetailView(RetrieveUpdateDestroyAPIView):
	queryset = Parcel.objects.all()
	serializer_class = ParcelSerializer
