import django_filters
from PhotoApp.models import Photo
from django.contrib.auth.models import User

class PhotoFilter(django_filters.FilterSet):
    user = django_filters.CharFilter(method='filter_user')
    captions = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Photo
        fields = ['user','captions']
    def filter_user(self, queryset, name, value):
        user_list = User.objects.all().filter(username=value)
        if len(user_list) > 0:
            user_obj = user_list[0]
            filtered_set = queryset.filter(user_id=user_obj.id)
        else:
            filtered_set = Photo.objects.none()
        return filtered_set

class MyPhotoFilter(django_filters.FilterSet):
    captions = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Photo
        fields = ['captions']