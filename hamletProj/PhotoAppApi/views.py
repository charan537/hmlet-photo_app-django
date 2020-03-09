from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PhotoSerializer
from PhotoApp.models import Photo
from .filters import PhotoListApiFilter,MyPhotoApiFilter
import django_filters
from rest_framework.exceptions import PermissionDenied
from datetime import datetime
from rest_framework.generics import ListAPIView

class PhotoListView(ListAPIView):
    queryset = Photo.objects.all().filter(saveAsDraft=False)
    serializer_class = PhotoSerializer
    filterset_class= PhotoListApiFilter

class PhotosViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    filterset_class= MyPhotoApiFilter

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Photo.objects.filter(user_id=user)
        raise PermissionDenied()
        
    def perform_create(self, serializer):
        if serializer.validated_data['saveAsDraft'] == True:
            serializer.save(user=self.request.user)
        else:
            serializer.save(user=self.request.user,publishedDate=datetime.now())

    def perform_update(self, serializer):
        if serializer.validated_data['saveAsDraft'] == True:
            serializer.save()
        else:
            serializer.save(publishedDate=datetime.now())