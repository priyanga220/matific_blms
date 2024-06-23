from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils.decorators import method_decorator

from core.models import Player, UserRole
from ..serializers import PlayerViewSerializer
from ..services import PlayerService
from ..decorators import has_permission


class PlayerDetail(APIView):
    playerservice = PlayerService()

    def get_object(self, pk):
        try:
            return Player.objects.get(pk=pk)
        except Player.DoesNotExist:
            raise Http404

    @method_decorator(has_permission([UserRole.ADMIN, UserRole.COACH]))
    def get(self, request, pk: int, format=None):
        serializer = PlayerViewSerializer(self.playerservice.loadPlayerView(pk))
        return Response(serializer.data)
