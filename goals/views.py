from dry_rest_permissions.generics import DRYPermissionFiltersBase
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from goals.models import Goal
from goals.serializers import GoalSerializer, GoalUpdateSerializer


class GoalFilterBackend(DRYPermissionFiltersBase):
    def filter_queryset(self, request, queryset, view):
        return queryset.filter(organization=request.user.organization)


class GoalViewSet(ModelViewSet):
    permissions_classes = (IsAuthenticated,)
    queryset = Goal.objects.all()
    lookup_field = "uuid"
    filter_backends = (GoalFilterBackend,)

    def get_serializer_class(self):
        if self.action.endswith("update"):
            return GoalUpdateSerializer
        else:
            return GoalSerializer
