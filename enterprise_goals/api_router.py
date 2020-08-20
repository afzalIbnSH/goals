from django.conf import settings
from django.conf.urls import include, url
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework.routers import SimpleRouter


router = SimpleRouter()

schema_view = get_schema_view(
    openapi.Info(
        title="Goals API",
        default_version="v1",
        description="Helps you manage your organization's goals",
        contact=openapi.Contact(email="aflibnush@gmail.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    url(r"^", include(router.urls)),
    url(
        r"^swagger/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]
