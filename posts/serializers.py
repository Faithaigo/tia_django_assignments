from rest_framework import serializers
from .models import Post,User


class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id","title","content","created_at","author_id"]