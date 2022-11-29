from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from .serializers import UserSerializer, PostSerializer, CommentSerializer
from blog.models import Post, Comment


# ViewSets define the view behavior.
class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
class PostRetrieveAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer