from rest_framework import serializers
from PhotoApp.models import Photo
        
class PhotoSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    publishedDate = serializers.ReadOnlyField()
    class Meta:
        model = Photo
        fields='__all__'