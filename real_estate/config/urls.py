"""real_estate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Real Estate API",
        default_version="v1",
        description="Real Estate API for iOS and android app",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="fertahrez@gmail.com"),
        license=openapi.License(name="Apache License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,)
)

urlpatterns = [
    path("realestateadmin/", admin.site.urls),
    path("api/", include('real_estate.apps.users.urls')),
    path("api/", include("real_estate.apps.profiles.urls")),
    path("api/", include("real_estate.apps.properties.urls")),
    path("api/", include("real_estate.apps.ratings.urls")),
    path("api/", include("real_estate.apps.enquiries.urls")),

    path('', schema_view.with_ui('swagger', cache_timeout=0), name="schema-swagger-ui"),
    path('docs/', schema_view.with_ui('redoc', cache_timeout=0), name="schema-redoc-ui")
]
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Real Estate Admin"
admin.site.site_title = "Real Estate Admin Portal"
admin.site.index_title = "Welcome to the Real Estate Portal"