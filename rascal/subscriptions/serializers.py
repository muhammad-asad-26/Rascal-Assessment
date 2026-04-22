from .models import SubscriptionDuration, PlanType
from rest_framework import serializers

class AddSubscriptionPlanSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255, required=True)
    plan_type = serializers.ChoiceField(choices=PlanType.choices, required=True)
    description = serializers.CharField(max_length=255, required=True)
    price = serializers.FloatField(required=True)
    duration = serializers.ChoiceField(choices=SubscriptionDuration.choices, required=True)

class AllSubscriptionPlanSerializer(serializers.Serializer):
    uuid = serializers.UUIDField(required=True)
    plan_type = serializers.ChoiceField(choices=PlanType.choices, required=True)
    description = serializers.CharField(max_length=255, required=True)
    price = serializers.FloatField(required=True)
    duration = serializers.ChoiceField(choices=SubscriptionDuration.choices, required=True)

class UserSubscriptionSerializer(serializers.Serializer):
    plan = AllSubscriptionPlanSerializer(read_only=True)
    status = serializers.CharField()
    start_date = serializers.DateTimeField()
    end_date = serializers.DateTimeField()
    is_expired = serializers.BooleanField()
