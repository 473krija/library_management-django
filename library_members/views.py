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

from rest_framework import generics
from .models import Fine
from .serializers import FineSerializer

# List all fines OR create new fine
class FineListCreateView(generics.ListCreateAPIView):
    queryset = Fine.objects.all()
    serializer_class = FineSerializer

# Retrieve, Update, Delete a specific fine
class FineDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Fine.objects.all()
    serializer_class = FineSerializer

