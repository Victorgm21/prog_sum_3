from django.shortcuts import render


from rest_framework import viewsets, permissions
from .models import cityTemperature
from .serializers import cityTemperatureSerializer

# Create your views here.

class cityTemperatureViewSet(viewsets.ModelViewSet):
    queryset = cityTemperature.objects.all()
    serializer_class = cityTemperatureSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

