from django.db import models
from django.db.models import fields
from rest_framework import serializers
from myapp.models.member import Member


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = "__all__"
