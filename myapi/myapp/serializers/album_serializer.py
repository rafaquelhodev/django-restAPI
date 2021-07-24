from django.db import models
from django.db.models import fields
from rest_framework import serializers
from myapp.models.album import Album


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = "__all__"
