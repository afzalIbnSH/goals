from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from enterprise_goals.models import EGBaseModel
from enterprise_goals.managers import EGDeleteManager
from users.managers import UserManager


class Organization(EGBaseModel):
    class Plan(models.TextChoices):
        FREE = "free", _("Free plan")
        ENTERPRISE = "enterprise", _("Enterprise plan")

    name = models.CharField(max_length=256)
    plan = models.CharField(max_length=16, choices=Plan.choices)


class EGUserManager(EGDeleteManager, UserManager):
    pass


class User(AbstractUser, EGBaseModel):
    username = None
    first_name = None
    last_name = None

    class Role(models.TextChoices):
        ADMIN = "admin", _("Admin user")
        STAFF = "staff", _("Staff user")

    name = models.CharField(max_length=256)
    email = models.EmailField(_("email address"), unique=True)
    organization = models.ForeignKey(
        Organization, on_delete=models.PROTECT, editable=False
    )
    role = models.CharField(max_length=16, choices=Role.choices)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = EGUserManager()

    def __str__(self):
        return self.email

    @staticmethod
    def has_write_permission(request):
        return (
            request.user.organization.plan == Organization.Plan.ENTERPRISE
            and request.user.role == User.Role.ADMIN
        )
