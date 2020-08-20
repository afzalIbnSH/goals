"""
Root URL Configuration
"""
import os
from django.contrib import admin
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from enterprise_goals import api_router


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include(api_router.urlpatterns)),
    path("api/v1/auth/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/v1/auth/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
