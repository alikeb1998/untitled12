from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers


# Create your views here.
class FishViewSet(viewsets.ModelViewSet):
    queryset = models.Fish.objects.all()
    serializer_class = serializers.FishSerializer


class AnimalViewSet(viewsets.ModelViewSet):
    queryset = models.animals.objects.all()
    serializer_class = serializers.AnimalSerializer
class mamadViewSet(viewsets.ModelViewSet):
    queryset = models.mamada.objects.all()
    serializer_class = serializers.MamadSerializer
