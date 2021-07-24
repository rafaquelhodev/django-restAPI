from django.db import models
from django.db.models import fields
from rest_framework import serializers
from myapp.models.band import Band


class BandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Band
        fields = "__all__"
