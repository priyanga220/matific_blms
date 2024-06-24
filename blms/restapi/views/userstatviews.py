from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils.decorators import method_decorator

from ..serializers import UserstatSerializer
from ..serializers import UserSerializer
from core.models import UserRole
from ..services import UserService
from ..decorators import has_permission


class Userstat(APIView):
    userservice = UserService()

    @method_decorator(has_permission([UserRole.ADMIN]))
    def get(self, request, format=None):
        serializer = UserstatSerializer(self.userservice.loadUserstats(), many=True)
        return Response(serializer.data)


class OnlineUsers(APIView):
    userservice = UserService()

    @method_decorator(has_permission([UserRole.ADMIN]))
    def get(self, request, format=None):
        serializer = UserSerializer(self.userservice.loadOnlineUsers(), many=True)
        return Response(serializer.data)
