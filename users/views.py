from dry_rest_permissions.generics import DRYPermissions
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from users.serializers import (
    RegistrationSerializer,
    UserCreateSerializer,
    UserReadSerializer,
)


class UserViewSet(CreateModelMixin, GenericViewSet):
    def get_permissions(self):
        if self.action == "registration":
            return []
        elif self.action == "current_user":
            return [
                IsAuthenticated(),
            ]
        else:
            return [
                IsAuthenticated(),
                DRYPermissions(),
            ]

    def get_serializer_class(self):
        if self.action == "registration":
            return RegistrationSerializer
        elif self.action == "current_user":
            return UserReadSerializer
        else:
            return UserCreateSerializer

    @action(detail=False, methods=["POST"])
    def registration(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    @action(detail=False, methods=["GET"])
    def current_user(self, request, *args, **kwargs):
        return Response(
            self.get_serializer(request.user, context={"request": request}).data
        )
