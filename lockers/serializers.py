from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from lockers.models import Locker


class LockerSerializer(ModelSerializer):
	size = serializers.CharField(source="get_size_display")

	class Meta:
		model = Locker
		fields = "__all__"
