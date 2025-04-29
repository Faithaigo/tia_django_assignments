from rest_framework import viewsets

from utils.slug import generate_unique_slug
from .serializers import CategorySerializer, TagSerializer, PostSerializer
from .models import Category, Tag, Post
from rest_framework.permissions import IsAuthenticated


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TagsViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class PostsViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        post = serializer.save(author=self.request.user,
                               slug=generate_unique_slug(Post, serializer.validated_data['title'])
                               )
        post.tags.set(serializer.validated_data['tags'])
