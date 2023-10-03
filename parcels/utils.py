from common_constants import SIZE_CHOICES


def get_size_display(locker_or_parsel):
	"""Maps the size integer to the human-readable string."""
	return dict(SIZE_CHOICES).get(locker_or_parsel.size, 'Unknown')