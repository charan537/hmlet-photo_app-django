import django_filters
from PhotoApp.filters import PhotoFilter
from PhotoApp.models import Photo
from django.contrib.auth.models import User
from django_filters import widgets

class PhotoApiFilter(PhotoFilter):
    saveAsDraft = django_filters.BooleanFilter(field_name='saveAsDraft')
    ordering = django_filters.OrderingFilter(fields=['publishedDate'], widget=widgets.LinkWidget)
    class Meta:
        model = Photo
        fields = ['user','captions','saveAsDraft','ordering']
