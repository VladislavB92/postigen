from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from parcels.models import Parcel
from lockers.models import Locker
import pytest
from django.test import TransactionTestCase
from dotenv import load_dotenv

client = APIClient()


class LockersTest(TransactionTestCase):

	@pytest.fixture(scope="class", autouse=True)
	def load_env(self):
		load_dotenv("../../.local.env")

	def test_get_lockers(self):
		url = reverse("locker_list_create")
		response = client.get(url)
		assert response.status_code == status.HTTP_200_OK

	def test_take_parcel_from_locker(self):
		locker = Locker.objects.create(location_address="Test Locker", size=2)
		parcel = Parcel.objects.create(size=2, locker=locker)
		url = reverse("take_parcel", kwargs={"pk": locker.id})
		data = {
			"parcel_id": parcel.id
		}
		response = client.put(url, data, format="json")
		assert response.status_code == status.HTTP_200_OK

	def test_take_non_existent_parcel_from_locker(self):
		locker = Locker.objects.create(location_address="Test Locker", size=2)
		url = reverse("take_parcel", kwargs={"pk": locker.id})
		data = {
			"parcel_id": 999
		}
		response = client.put(url, data, format="json")
		assert response.status_code == status.HTTP_404_NOT_FOUND

	def test_take_parcel_from_wrong_locker(self):
		locker1 = Locker.objects.create(location_address="Locker 1", size=2)
		locker2 = Locker.objects.create(location_address="Locker 2", size=2)
		parcel = Parcel.objects.create(size=2, locker=locker1)
		url = reverse("take_parcel", kwargs={"pk": locker2.id})
		data = {
			"parcel_id": parcel.id
		}
		response = client.put(url, data, format="json")
		assert response.status_code == status.HTTP_400_BAD_REQUEST
