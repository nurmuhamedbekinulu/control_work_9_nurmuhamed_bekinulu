from django.views import View
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

# from api.serializers import ArticleSerializer
# from webapp.models import Article

# class ArticleSimpleView(View):
    
#     def  get(self, request, *args, **kwargs):
#         object = Article.objects.all()
#         serializer = ArticleSerializer(object, many=True)
#         return JsonResponse(serializer.data)


# class ArticleView(APIView):
    
#     def  get(self, request, *args, **kwargs):
#         object = Article.objects.all()
#         serializer = ArticleSerializer(object, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
