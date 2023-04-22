from rest_framework import serializers
from webapp.models.photos import Photo


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('id', 'photo', 'caption', 'author', 'created_at', 'updated_at')
        read_only_fields = ('id', 'photo', 'caption', 'author', 'created_at', 'updated_at')
    

