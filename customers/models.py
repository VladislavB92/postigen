from django.db import models


class Customer(models.Model):
	"""Customer models that serves as sender and receiver."""

	email = models.EmailField()
	phone = models.CharField(max_length=20, blank=True)

	def __str__(self):
		return f"{self.email}"
