from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ParcelDetailViewSet

router = DefaultRouter()
router.register(r"", ParcelDetailViewSet)

urlpatterns = [
	path("", include(router.urls)),
]
