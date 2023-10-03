from django.db import models
from postigen.common_constants import SIZE_CHOICES, STATUS_CHOICES


class Locker(models.Model):
	"""Locker model."""

	location_address = models.CharField(
		max_length=128,
		null=False,
		blank=False,
	)
	locker_size = models.CharField(
		max_length=2,
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
