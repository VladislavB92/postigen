from rest_framework.generics import (
	ListCreateAPIView,
	RetrieveUpdateDestroyAPIView,
)
from .models import Locker
from .serializers import LockerSerializer


class LockerListCreateView(ListCreateAPIView):
	queryset = Locker.objects.all()
	serializer_class = LockerSerializer


class LockerDetailView(RetrieveUpdateDestroyAPIView):
	queryset = Locker.objects.all()
	serializer_class = LockerSerializer
