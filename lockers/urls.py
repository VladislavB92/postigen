from django.urls import path
from .views import LockerListCreateView, LockerDetailView

urlpatterns = [
	path(
		"",
		LockerListCreateView.as_view(),
		name="locker-list-create",
	),
	path(
		"<int:pk>/",
		LockerDetailView.as_view(),
		name="locker-detail",
	),
]
