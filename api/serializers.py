from rest_framework import serializers
from webapp.models.articles import Article, StatusChoice


class CommentsSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=1000, min_length=5, required=True, allow_blank=True)
    author = serializers.CharField(max_length=200, required=True, allow_blank=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)




# class ArticleSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(max_length=200, required=True, allow_blank=True)
#     text = serializers.CharField(max_length=1000, min_length=5, required=True, allow_blank=True)
#     author = serializers.CharField(max_length=200, required=True, allow_blank=True)
#     status = serializers.ChoiceField(choices=StatusChoice, required=False, default=StatusChoice.ACTIVE)
#     created_at = serializers.DateTimeField(read_only=True)
#     updated_at = serializers.DateTimeField(read_only=True)
#     comments = CommentsSerializer(many=True, read_only=True)

class ArticleSerializer(serializers.ModelSerializer):
    comments = CommentsSerializer(many=True, read_only=True)
    class Meta:
        model = Article
        fields = ('id', 'title', 'author', 'created_at', 'updated_at', 'comments')
        read_only_fields = ('id', 'created_at', 'updated_at', 'comments')
    

    # def create(self, validate_data):
    #     return Article.objects.create(**validate_data)    


    # def update(self, instance: Article, validate_data):
    #     for field, value in validate_data.items():
    #         setattr(instance, field, value)
    #     instance.save()
    #     return instance
    

