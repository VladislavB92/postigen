from rest_framework import status
from rest_framework.decorators import action
from rest_framework.generics import (
	ListCreateAPIView,
)
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from lockers.models import Locker
from .models import Parcel
from .serializers import ParcelSerializer


class ParcelListCreateView(ListCreateAPIView):
	queryset = Parcel.objects.all()
	serializer_class = ParcelSerializer


class ParcelDetailViewSet(ModelViewSet):
	queryset = Parcel.objects.all()
	serializer_class = ParcelSerializer
	authentication_classes = []
	permission_classes = [AllowAny]

	@action(detail=True, methods=["put"], url_path="put-parcel")
	def put_parcel_to_locker(self, request, pk=None):
		parcel = self.get_object()
		locker_id = request.data.get("locker_id")

		try:
			locker = Locker.objects.get(pk=locker_id)
		except Locker.DoesNotExist:
			return Response(
				{
					"error": "Locker not found"
				},
				status=status.HTTP_404_NOT_FOUND,
			)
		parcel.locker = locker
		parcel.save()
		return Response(
			{
				"message": "Parcel placed in the locker at "
						   f"ID {parcel.locker.id} - "
						   f"{parcel.locker.location_address} successfully"
			},
			status=status.HTTP_200_OK
		)

	@action(detail=True, methods=["put"], url_path="move-parcel")
	def move_parcel_between_lockers(self, request, pk=None):
		parcel = self.get_object()
		old_locker = parcel.locker
		new_locker_id = request.data.get("new_locker_id")

		try:
			new_locker = Locker.objects.get(pk=new_locker_id)
		except Locker.DoesNotExist:
			return Response(
				{
					"error": "New locker not found"
				},
				status=status.HTTP_404_NOT_FOUND,
			)

		parcel.locker = new_locker
		parcel.save()
		return Response(
			{
				"message": f"Parcel moved from {old_locker.id} - "
						   f"{old_locker.location_address} to a new locker "
						   f"{new_locker_id} - "
						   f"{new_locker.location_address} successfully",
			},
			status=status.HTTP_200_OK,
		)
