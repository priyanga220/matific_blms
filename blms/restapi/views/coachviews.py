from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.models import Coach
from ..serializers import CoachSerializerFull


class CoachList(APIView):
    def get(self, request, format=None):
        coaches = Coach.objects.all()
        serializer = CoachSerializerFull(coaches, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CoachSerializerFull(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
