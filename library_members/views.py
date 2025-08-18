from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets

class MemberProfileViewSet(viewsets.ModelViewSet):
    queryset = MemberProfile.objects.all()
    serializer_class = MemberProfileSerializer

class ReadingClubViewSet(viewsets.ModelViewSet):
    queryset = ReadingClub.objects.all()
    serializer_class = ReadingClubSerializer
