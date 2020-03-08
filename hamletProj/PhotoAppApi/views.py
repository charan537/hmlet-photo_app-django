from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PhotoSerializer
from PhotoApp.models import Photo
from .filters import PhotoApiFilter
import django_filters

class PhotosViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    filterset_class= PhotoApiFilter