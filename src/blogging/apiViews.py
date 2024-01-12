from django.contrib.auth import get_user_model 
from rest_framework import viewsets
from .models import Post, Category
from .permissions import IsAuthorOrReadOnly
from rest_framework.permissions import IsAuthenticated
from .serializers import PostSerializer, CategorySerializer, UserSerializer

class PostViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthorOrReadOnly,]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CategoryViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated,]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class UserViewset(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


