from uuid import uuid4

from django.db import models


from enterprise_goals.managers import EGDeleteManager


class EGBaseModel(models.Model):
    uuid = models.UUIDField(default=uuid4, unique=True, db_index=True, editable=False)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)

    objects = EGDeleteManager()

    class Meta:
        abstract = True

    def delete(self, *args):
        self.deleted = True
        self.save()
