from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response

from ..serializers import UserstatSerializer
from ..serializers import UserSerializer

from ..services import UserService


class Userstat(APIView):
    userservice = UserService()

    def get(self, request, format=None):
        serializer = UserstatSerializer(self.userservice.loadUserstats(), many=True)
        return Response(serializer.data)


class OnlineUsers(APIView):
    userservice = UserService()

    def get(self, request, format=None):
        serializer = UserSerializer(self.userservice.loadOnlineUsers(), many=True)
        return Response(serializer.data)
