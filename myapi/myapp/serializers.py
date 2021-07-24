from django.db import models
from django.db.models import fields
from rest_framework import serializers
from myapp.models.music import Music


class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = "__all__"
