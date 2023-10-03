from django.urls import path
from .views import ParcelListCreateView, ParcelDetailView

urlpatterns = [
	path(
		"",
		ParcelListCreateView.as_view(),
		name="parcel-list-create",
	),
	path(
		"<int:pk>/",
		ParcelDetailView.as_view(),
		name="parcel-detail",
	),
]
