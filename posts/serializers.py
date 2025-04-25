from rest_framework import serializers
from django.utils.text import slugify
from .models import Category, Tag



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