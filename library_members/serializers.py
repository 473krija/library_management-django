from rest_framework import serializers
from .models import *

class MemberProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MemberProfile
        fields = "__all__"

class ReadingClubSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ReadingClub
        fields = "__all__"
