from django.urls import path

from .views import (
	MoveParcelView,
	ParcelDetailsView,
	PutParcelView,
	ParcelListCreateView,
)

urlpatterns = [
	path("", ParcelListCreateView.as_view(), name="parcel_list_create"),
	path("<int:pk>/", ParcelDetailsView.as_view(), name="parcel_details"),
	path("<int:pk>/put-parcel/", PutParcelView.as_view(), name="put_parcel"),
	path("<int:pk>/move-parcel/", MoveParcelView.as_view(), name="move_parcel"),
]
