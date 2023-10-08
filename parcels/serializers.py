from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from customers.serializers import CustomerSerializer
from customers.models import Customer
from .models import Parcel


class ParcelSerializer(ModelSerializer):
	size = serializers.SerializerMethodField()
	sender = CustomerSerializer(many=True)
	receiver = CustomerSerializer(many=True)

	class Meta:
		model = Parcel
		fields = "__all__"

	def get_size(self, obj):
		return obj.get_size_display()

	def create(self, validated_data):
		sender_data = validated_data.pop("sender")
		receiver_data = validated_data.pop("receiver")
		parcel = Parcel.objects.create(**validated_data)

		for sender_item in sender_data:
			sender, _ = Customer.objects.get_or_create(**sender_item)
			parcel.sender.add(sender)

		for receiver_item in receiver_data:
			receiver, _ = Customer.objects.get_or_create(**receiver_item)
			parcel.receiver.add(receiver)

		return parcel
