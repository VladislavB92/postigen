from rest_framework import status
from rest_framework.generics import (
	ListCreateAPIView,
	RetrieveAPIView,
	UpdateAPIView,
)
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from parcels.models import Parcel
from .models import Locker
from .serializers import LockerSerializer


class LockerListCreateView(ListCreateAPIView):
	queryset = Locker.objects.all()
	serializer_class = LockerSerializer
	authentication_classes = []
	permission_classes = [AllowAny]


class LockerDetailsView(RetrieveAPIView):
	queryset = Locker.objects.all()
	serializer_class = LockerSerializer
	authentication_classes = []
	permission_classes = [AllowAny]


class LockerTakeParcelView(UpdateAPIView):
	queryset = Locker.objects.all()
	serializer_class = LockerSerializer
	authentication_classes = []
	permission_classes = [AllowAny]

	def put(self, request, pk=None, *args, **kwargs):
		locker = self.queryset.get(pk=pk)
		parcel_id = request.data.get("parcel_id")

		try:
			parcel = Parcel.objects.get(pk=parcel_id)
		except Parcel.DoesNotExist:
			return Response(
				{
					"error": "Parcel not found"
				},
				status=status.HTTP_404_NOT_FOUND
			)

		if parcel.locker != locker:
			return Response({
				"error": "Parcel is not in this locker"
			},
				status=status.HTTP_400_BAD_REQUEST,
			)

		parcel.locker = None
		parcel.save()
		return Response({
			"message": "Parcel taken from locker successfully"
		},
			status=status.HTTP_200_OK,
		)
