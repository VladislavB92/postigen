from django.urls import path
from .views import (
	LockerTakeParcelView,
	LockerListCreateView,
	LockerDetailsView,
)

urlpatterns = [
	path("", LockerListCreateView.as_view(), name="locker_list_create"),
	path("<int:pk>/", LockerDetailsView.as_view(), name="parcel_details"),
	path("<int:pk>/take-parcel/", LockerTakeParcelView.as_view(), name="take_parcel"),
]
