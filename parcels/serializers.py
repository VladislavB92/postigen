from rest_framework.serializers import ModelSerializer
from .models import Parcel


class ParcelSerializer(ModelSerializer):
	class Meta:
		model = Parcel
		fields = "__all__"
