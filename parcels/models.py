from django.db import models
from lockers.models import Locker
from postigen.common_constants import SIZE_CHOICES
from customers.models import Customer


class Parcel(models.Model):
	"""
	Parcel model.
	Includes sender and receiver as unite Customer model.
	"""

	sender = models.ManyToManyField(
		Customer,
		related_name="sender",
	)
	receiver = models.ManyToManyField(
		Customer,
		related_name="receiver",
	)
	parcel_size = models.CharField(
		max_length=2,
		choices=SIZE_CHOICES,
		null=False,
		blank=False,
	)
	locker = models.ForeignKey(
		Locker,
		models.PROTECT,
		null=False,
		blank=False,
	)
