from django.urls import path
from .views import (
	CustomerListCreateView,
	CustomerDetailView,
)

urlpatterns = [
	path(
		"",
		CustomerListCreateView.as_view(),
		name="customer_list_create",
	),
	path(
		"<int:pk>/",
		CustomerDetailView.as_view(),
		name="customer_detail",
	),
]
