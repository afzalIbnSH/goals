from django.utils.timezone import now
from rest_framework import serializers

from goals.models import Goal


class GoalSerializer(serializers.ModelSerializer):
    done = serializers.BooleanField(read_only=True)

    class Meta:
        model = Goal
        fields = ("uuid", "short_description", "details", "target", "done")

    def create(self, validated_data):
        validated_data["organization"] = self.context["request"].user.organization
        return super().create(validated_data)


class GoalUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = ("uuid", "short_description", "details", "target", "done")

    def update(self, goal, validated_data):
        if not goal.done and validated_data["done"]:
            goal.done_on = now()
        return super().update(goal, validated_data)
