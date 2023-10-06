from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from lockers.models import Locker
from parcels.serializers import ParcelSerializer


class LockerSerializer(ModelSerializer):
	size = serializers.CharField(source="get_size_display")
	parcels = ParcelSerializer(many=True, read_only=True, source="parcel_set")

	class Meta:
		model = Locker
		fields = "__all__"
