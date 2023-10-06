from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from customers.serializers import CustomerSerializer
from .models import Parcel


class ParcelSerializer(ModelSerializer):
	size = serializers.CharField(source="get_size_display")
	sender = CustomerSerializer(many=True)
	receiver = CustomerSerializer(many=True)

	class Meta:
		model = Parcel
		fields = "__all__"
