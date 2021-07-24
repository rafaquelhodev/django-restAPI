from rest_framework import generics
from .serializers import MusicSerializer
from .models import Music


class MusicList(generics.ListCreateAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
