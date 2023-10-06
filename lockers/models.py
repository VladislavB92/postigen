from django.db import models
from postigen.common_constants import SIZE_CHOICES, STATUS_CHOICES
from parcels.utils import get_size_display


class Locker(models.Model):
	"""Locker model."""

	location_address = models.CharField(
		max_length=128,
		null=False,
		blank=False,
	)
	size = models.IntegerField(
		choices=SIZE_CHOICES,
		null=False,
		blank=False,
	)
	status = models.CharField(
		max_length=12,
		choices=STATUS_CHOICES,
		default="free",
		null=False,
		blank=False,
	)

	def __str__(self):
		return f"{self.id} - {self.location_address} - {get_size_display(self)}"
