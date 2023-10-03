from django.db import models
from customers.models import Customer

PARCEL_SIZE_CHOICES = [
	("XS", "Extra Small"),
	("S", "Small"),
	("M", "Medium"),
	("L", "Large"),
	("XL", "Extra Large"),
]


class Parcel(models.Model):
	"""Parcel model."""

	sender = models.ManyToManyField(
		Customer,
		related_name="sender",
	)
	receiver = models.ManyToManyField(
		Customer,
		related_name="receiver",
	)
	parcel_size = models.CharField(
		max_length=11,
		choices=PARCEL_SIZE_CHOICES,
		null=False,
		blank=False,
	)
