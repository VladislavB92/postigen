from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from customers.models import Customer
from django.test import TransactionTestCase
import pytest
from dotenv import load_dotenv

client = APIClient()


class CustomersTest(TransactionTestCase):

	@pytest.fixture(scope="class", autouse=True)
	def load_env(self):
		load_dotenv("../../.local.env")

	def test_get_customers(self):
		url = reverse("customer_list_create")
		response = client.get(url)
		assert response.status_code == status.HTTP_200_OK

	def test_create_customer(self):
		url = reverse("customer_list_create")
		customer_data = {
			"email": "johndoe@example.com",
			"phone": "+37122222222",
		}
		response = client.post(url, customer_data, format="json")
		assert response.status_code == status.HTTP_201_CREATED

	def test_get_customer_detail(self):
		customer = Customer.objects.create(
			email="janesmith@example.com",
			phone="+37122222222",
		)
		url = reverse("customer_detail", kwargs={"pk": customer.id})
		response = client.get(url)
		assert response.status_code == status.HTTP_200_OK

	def test_update_customer(self):
		customer = Customer.objects.create(
			email="janesmith@example.com",
			phone="+37122222222",
		)
		url = reverse("customer_detail", kwargs={"pk": customer.id})
		updated_data = {
			"email": "updated@example.com",
		}
		response = client.put(url, updated_data, format="json")
		assert response.status_code == status.HTTP_200_OK

	def test_delete_customer(self):
		customer = Customer.objects.create(
			email="janesmith@example.com",
			phone="+37122222222",
		)
		url = reverse("customer_detail", kwargs={"pk": customer.id})
		response = client.delete(url)
		assert response.status_code == status.HTTP_204_NO_CONTENT
