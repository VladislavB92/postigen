from django.db import models


class Customer(models.Model):
	"""Customer models that serves as sender and receiver."""

	email = models.EmailField()
	phone = models.CharField(max_length=20, blank=True)

	def __str__(self):
		return f"{self.email}"


	def sanitize_phone_number(self):
		self.phone = self.phone.replace(" ", "")

	def save(self, *args, **kwargs):
		self.sanitize_phone_number()
		super().save(*args, **kwargs)
