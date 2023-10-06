from django.urls import path
from .views import LockerDetailView, LockerListCreateView

urlpatterns = [
	path("", LockerListCreateView.as_view(), name="locker_list_create"),
	path("<int:pk>/take-parcel/", LockerDetailView.as_view(), name="take_parcel"),
]
