from django.shortcuts import render
from app.models import Actor,Details
from .serializers import DetailsSerializer, ActorSerializer
from rest_framework import generics
# Create your views here.

class ActorDetailView(generics.ListCreateAPIView):
    serializer_class = ActorSerializer
    queryset = Actor.objects.all()

class ActorUpdateView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ActorSerializer
    queryset = Actor.objects.all()

class DetailsInfoView(generics.ListCreateAPIView):
    serializer_class = DetailsSerializer
    queryset = Details.objects.all()

class DetailsUpdateView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DetailsSerializer
    queryset = Details.objects.all()


