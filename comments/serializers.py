from rest_framework import serializers
from .models import Comment


class CommentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id','comment', 'post','author', 'created_at']
        read_only_fields = ['post','created_at']

    def create(self, validated_data):
        comment = Comment(
            comment = validated_data['comment'],
            author = validated_data['author'],
            post_id = self.context.get('view').kwargs.get('post_id')
        )
        comment.save()
        return comment