from django.urls import path
from django.contrib import admin
from .views import (
	CustomerListCreateView,
	CustomerDetailView,
)

admin.site.site_header = "POSTIGEN"
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
