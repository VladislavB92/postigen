from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from lockers.models import Locker
from parcels.models import Parcel
import pytest
from django.test import TransactionTestCase
from dotenv import load_dotenv

client = APIClient()


class ParcelsTest(TransactionTestCase):

	@pytest.fixture(scope="class", autouse=True)
	def load_env(self):
		load_dotenv("../../.local.env")

	def test_get_parcels(self):
		url = reverse("parcel_list_create")
		response = client.get(url)
		assert response.status_code == status.HTTP_200_OK

	def test_move_parcel_to_locker(self):
		parcel = Parcel.objects.create(size=2)
		locker = Locker.objects.create(location_address="Test Locker", size=2)
		url = reverse("move_parcel", kwargs={"pk": parcel.id})
		data = {
			"new_locker_id": locker.id
		}
		response = client.put(url, data, format="json")
		assert response.status_code == status.HTTP_200_OK

	def test_move_non_existent_parcel_to_locker(self):
		locker = Locker.objects.create(location_address="Test Locker", size=2)
		url = reverse("move_parcel", kwargs={"pk": 999})
		data = {
			"new_locker_id": locker.id
		}
		response = client.put(url, data, format="json")
		assert response.status_code == status.HTTP_404_NOT_FOUND

	def test_put_parcel_to_locker(self):
		locker = Locker.objects.create(location_address="Test Locker", size=2)
		parcel = Parcel.objects.create(size=2, locker=None)
		url = reverse("put_parcel", kwargs={"pk": parcel.id})
		data = {
			"locker_id": locker.id
		}
		response = client.put(url, data, format="json")
		assert response.status_code == status.HTTP_200_OK

	def test_put_parcel_to_non_existent_locker(self):
		parcel = Parcel.objects.create(size=2, locker=None)
		url = reverse("put_parcel", kwargs={"pk": parcel.id})
		data = {
			"locker_id": 999
		}
		response = client.put(url, data, format="json")
		assert response.status_code == status.HTTP_404_NOT_FOUND

	def test_put_parcel_to_locker_with_occupied_status(self):
		locker = Locker.objects.create(
			location_address="Test Locker",
			size=2,
			status="occupied",
		)
		parcel = Parcel.objects.create(size=2, locker=None)
		url = reverse("put_parcel", kwargs={"pk": parcel.id})
		data = {
			"locker_id": locker.id
		}
		response = client.put(url, data, format="json")
		assert response.status_code == status.HTTP_400_BAD_REQUEST

	def test_put_parcel_to_locker_with_size_exceeds_locker(self):
		locker = Locker.objects.create(location_address="Test Locker", size=1)
		parcel = Parcel.objects.create(size=2, locker=None)
		url = reverse("put_parcel", kwargs={"pk": parcel.id})
		data = {
			"locker_id": locker.id
		}
		response = client.put(url, data, format="json")
		assert response.status_code == status.HTTP_400_BAD_REQUEST
