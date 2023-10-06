from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from rest_framework.exceptions import ValidationError
from lockers.models import Locker
from postigen.common_constants import SIZE_CHOICES, STATUS_CHOICES
from customers.models import Customer
from utils import get_size_display


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
	size = models.IntegerField(
		choices=SIZE_CHOICES,
		null=False,
		blank=False,
	)
	locker = models.ForeignKey(
		Locker,
		models.PROTECT,
		null=True,
		blank=True,
	)

	def __str__(self):
		return f"Parcel ID {self.id}"

	def clean(self):
		if self.locker:
			if self.locker.status != "free":
				raise ValidationError(
					{
						"status": "The locker is not available: "
								  f"{self.locker.status}",
					}
				)
			if self.size > self.locker.size:
				raise ValidationError(
					{
						"size": "The size of the parcel exceeds "
								"locker's size: "
								f"{get_size_display(self)} "
								f"> {get_size_display(self.locker)}",
					}
				)

	def save(self, *args, **kwargs):
		self.full_clean()
		if self.locker:
			self.locker.status = STATUS_CHOICES[1][0]  # busy
			self.locker.save()
		return super().save(*args, **kwargs)


@receiver(pre_save, sender=Parcel)
def update_locker_status(sender, instance, **kwargs):
	"""
	Model signal that makes the locker's status empty
	when the parcel has been taken out,
	before saving the parcels instance.
	"""
	try:
		original_instance = Parcel.objects.get(pk=instance.pk)
		if original_instance.locker:
			previous_locker = original_instance.locker
			previous_locker.status = STATUS_CHOICES[0][0] # free
			previous_locker.save()
	except Parcel.DoesNotExist as e:
		return {
			"parcel": f"{e}",
		}
