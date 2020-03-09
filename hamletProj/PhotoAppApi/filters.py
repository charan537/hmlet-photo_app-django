import django_filters
from PhotoApp.filters import PhotoFilter,MyPhotoFilter
from PhotoApp.models import Photo
from django.contrib.auth.models import User
from django_filters import widgets

class PhotoListApiFilter(PhotoFilter):
    ordering = django_filters.OrderingFilter(fields=['publishedDate'], widget=widgets.LinkWidget)
    class Meta:
        model = Photo
        fields = ['user','captions','ordering']

class MyPhotoApiFilter(MyPhotoFilter):
    saveAsDraft = django_filters.BooleanFilter(field_name='saveAsDraft')
    ordering = django_filters.OrderingFilter(fields=['publishedDate'], widget=widgets.LinkWidget)
    class Meta:
        model = Photo
        fields = ['captions','saveAsDraft','ordering']