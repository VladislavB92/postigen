from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	path("admin/", admin.site.urls),
	path("api-auth/", include('rest_framework.urls')),
	path("api/parcels/", include("parcels.urls")),
	path("api/lockers/", include("lockers.urls")),
	path("api/customers/", include("customers.urls")),
]
