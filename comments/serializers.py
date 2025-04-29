from rest_framework import serializers
from .models import Comment


class CommentsSerializers(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        fields = ['id','comment', 'post','author', 'created_at']
        read_only_fields = ['post','created_at']
