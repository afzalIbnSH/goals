from django.db import models


class EGDeleteManager(models.Manager):
    """
    Custom manager taking care of filtering out soft deleted rows.
    """

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(deleted=False)
