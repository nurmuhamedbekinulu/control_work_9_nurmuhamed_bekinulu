from django.views import View
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from webapp.models.photos import Photo
from api.serializers import PhotoSerializer

class PhotoView(APIView):
    
    def  get(self, request, *args, **kwargs):
        object = Photo.objects.all()
        serializer = PhotoSerializer(object, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
