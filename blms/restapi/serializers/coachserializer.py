from rest_framework import serializers
from core.models import Coach


# Serilizer for coach reference (id, name)
class CoachReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coach
        fields = ["id", "name"]


class CoachSerializerFull(serializers.ModelSerializer):
    team = serializers.StringRelatedField()

    class Meta:
        model = Coach
        # fields = "__all__"
        fields = ["name", "team", "created_date"]
