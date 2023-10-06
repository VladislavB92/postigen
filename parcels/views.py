from django.db.models.signals import pre_save
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from lockers.models import Locker
from .models import Parcel
from .serializers import ParcelSerializer


class ParcelListCreateView(ListCreateAPIView):
	queryset = Parcel.objects.all()
	serializer_class = ParcelSerializer


class PutParcelView(UpdateAPIView):
	queryset = Parcel.objects.all()
	serializer_class = ParcelSerializer
	authentication_classes = []
	permission_classes = [AllowAny]

	def put(self, request, pk=None, *args, **kwargs):
		parcel = self.queryset.get(pk=pk)
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
						   "ID {parcel.locker.id} -{parcel.locker.location_address} successfully"
			},
			status=status.HTTP_200_OK
		)


class MoveParcelView(UpdateAPIView):
	queryset = Parcel.objects.all()
	serializer_class = ParcelSerializer
	authentication_classes = []
	permission_classes = [AllowAny]

	def put(self, request, pk=None, *args, **kwargs):
		parcel = self.queryset.filter(pk=pk).first()
		new_locker_id = int(request.data.get("new_locker_id"))

		if not parcel:
			return Response(
				{
					"error": "Parcel not found"
				},
				status=status.HTTP_404_NOT_FOUND,
			)
		if parcel.locker_id == new_locker_id:
			return Response(
				{
					"message": "Parcel is already in the destination locker",
				},
				status=status.HTTP_200_OK,
			)
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
		pre_save.send(sender=Parcel, instance=parcel)
		parcel.save()
		return Response(
			{
				"message": f"Parcel moved from to a new locker "
						   f"{new_locker_id} - "
						   f"{new_locker.location_address} successfully",
			},
			status=status.HTTP_200_OK,
		)
