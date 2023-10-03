from rest_framework.serializers import ModelSerializer
from lockers.models import Locker


class LockerSerializer(ModelSerializer):
	class Meta:
		model = Locker
		fields = "__all__"
