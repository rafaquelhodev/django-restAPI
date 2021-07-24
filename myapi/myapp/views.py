from rest_framework import generics
from myapp.serializers import MusicSerializer
from myapp.models.music import Music


class MusicList(generics.ListCreateAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
