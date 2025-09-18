from rest_framework import serializers
from .models import *

class MemberProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberProfile
        fields = "__all__"

class ReadingClubSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ReadingClub
        fields = "__all__"

from rest_framework import serializers
from .models import Fine

class FineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fine
        fields = "__all__"

