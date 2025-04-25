from rest_framework import serializers
from django.utils.text import slugify
from .models import Category, Tag,Post
from utils.slug import generate_unique_slug



class CategorySerializer(serializers.ModelSerializer):
    slug = serializers.CharField(read_only=True)
    class Meta:
        model = Category
        fields = ['id','name','slug']

    def create(self, validated_data):
        category = Category(
            name=validated_data['name'],
            slug = slugify(validated_data['name'])
        )
        category.save()
        return category

class TagSerializer(serializers.ModelSerializer):
    slug = serializers.CharField(read_only=True)
    class Meta:
        model = Tag
        fields = ['id','name','slug']

    def create(self, validated_data):
        tag = Tag(
            name=validated_data['name'],
            slug=slugify(validated_data['name'])
        )
        tag.save()
        return tag

class PostSerializer(serializers.ModelSerializer):

    # TODO: Get author, category and tags data

    class Meta:
        model = Post
        fields = ['id','title','content','slug','created_at','author','category','tags']
        read_only_fields = ['slug','created_at']

    def create(self, validated_data):
        post = Post(
            title=validated_data['title'],
            content=validated_data['content'],
            author=validated_data['author'],
            category=validated_data['category'],
            slug = generate_unique_slug(Post, validated_data['title'])
        )
        post.save()
        post.tags.set(validated_data['tags'])
        return post