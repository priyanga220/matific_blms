from rest_framework import serializers
from core.models import UserRole


class UserstatSerializer(serializers.Serializer):
    userid = serializers.CharField(required=False, source="user__id")
    first_name = serializers.CharField(required=False, source="user__last_name")
    last_name = serializers.CharField(required=False, source="user__last_name")
    username = serializers.CharField(required=False, source="user__username")
    user_role = serializers.ChoiceField(
        required=False, choices=UserRole.ROLE_CHOICES, source="user__userrole"
    )


class UserSerializer(serializers.Serializer):
    first_name = serializers.CharField(required=False, default="")
    last_name = serializers.CharField(required=False, default="")
    email = serializers.CharField(required=False, default="")
    username = serializers.CharField(required=False, default="")
