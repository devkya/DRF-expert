from rest_framework import serializers
from django.contrib.auth.models import User
from blog.models import Post, Comment


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']
        
        
class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'image', 'like', 'category']
        
        
class PostRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = ['create_dt']
        
        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        
        
        