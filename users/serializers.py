from rest_framework import serializers

from users.models import Organization, User


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ("name", "plan")


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, style={"input_type": "password"})
    organization = OrganizationSerializer()

    class Meta:
        model = User
        fields = ("name", "email", "password", "organization")

    def create(self, validated_data):
        org_serializer = OrganizationSerializer(data=validated_data.pop("organization"))
        org_serializer.is_valid(raise_exception=True)
        return User.objects.create_user(
            validated_data.pop("email"),
            validated_data.pop("password"),
            organization=org_serializer.save(),
            role=User.Role.ADMIN,
            **validated_data,
        )


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, style={"input_type": "password"})

    class Meta:
        model = User
        fields = (
            "name",
            "email",
            "password",
        )

    def create(self, validated_data):
        return User.objects.create_user(
            validated_data.pop("email"),
            validated_data.pop("password"),
            organization=self.context["request"].user.organization,
            role=User.Role.STAFF,
            **validated_data,
        )


class UserReadSerializer(serializers.ModelSerializer):
    organization = OrganizationSerializer()

    class Meta:
        model = User
        fields = ("name", "email", "organization")
