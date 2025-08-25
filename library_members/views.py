from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets
from django.shortcuts import render, get_object_or_404, redirect

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

# List all members
def member_list(request):
    members = MemberProfile.objects.all()
    return render(request, "member_list.html", {"members": members})


# Member details
def member_detail(request, pk):
    member = get_object_or_404(MemberProfile, pk=pk)
    return render(request, "member_detail.html", {"member": member})


# List all clubs
def club_list(request):
    clubs = ReadingClub.objects.all()
    return render(request, "club_list.html", {"clubs": clubs})


# Club details
def club_detail(request, pk):
    club = get_object_or_404(ReadingClub, pk=pk)
    return render(request, "club_detail.html", {"club": club})


# List fines
def fine_list(request):
    fines = Fine.objects.all()
    return render(request, "fine_list.html", {"fines": fines})


# Fine details
def fine_detail(request, pk):
    fine = get_object_or_404(Fine, pk=pk)
    return render(request, "fine_detail.html", {"fine": fine})

