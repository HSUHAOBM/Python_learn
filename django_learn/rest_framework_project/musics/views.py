# Create your views here.
from musics.models import Music
from musics.models import fun_raw_sql_query

from musics.serializers import MusicSerializer

from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.decorators import action


# Create your views here.
class MusicViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer

    # /api/music/all_singer/
    @action(detail=False, methods=['get'])
    def all_singer(self, request):
        music = Music.objects.values_list('singer', flat=True).distinct()
        return Response(music, status=status.HTTP_200_OK)


    # /api/music/raw_sql_query/
    @action(detail=False, methods=['get'])
    def raw_sql_query(self, request):
        song = request.query_params.get('song', None)
        music = fun_raw_sql_query(song=song)
        serializer = MusicSerializer(music, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


from rest_framework.views import APIView

class HelloView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)