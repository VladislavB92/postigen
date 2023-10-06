from rest_framework import status
from rest_framework.decorators import action
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from parcels.models import Parcel
from .models import Locker
from .serializers import LockerSerializer


class LockerListCreateView(ListCreateAPIView):
	queryset = Locker.objects.all()
	serializer_class = LockerSerializer


class LockerDetailView(ModelViewSet):
	queryset = Locker.objects.all()
	serializer_class = LockerSerializer
	authentication_classes = []
	permission_classes = [AllowAny]

	@action(detail=True, methods=["put"], url_path="take-parcel")
	def take_parcel_from_locker(self, request, pk=None):
		locker = self.get_object()
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
