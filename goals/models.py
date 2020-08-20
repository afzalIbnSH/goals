from django.db import models

from enterprise_goals.models import EGBaseModel
from enterprise_goals.managers import EGDeleteManager
from users.models import Organization


class Goal(EGBaseModel):
    organization = models.ForeignKey(
        Organization, on_delete=models.PROTECT, editable=False
    )
    short_description = models.CharField(max_length=64)
    details = models.TextField(null=True)
    target = models.DateTimeField(null=True)
    done = models.BooleanField(default=False)
    done_on = models.DateTimeField(null=True)

    objects = EGDeleteManager()
