from rest_framework import generics
from .models import Comment
from .serializers import CommentsSerializers


class PostCommentsView(generics.ListCreateAPIView):
    serializer_class = CommentsSerializers

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        return Comment.objects.filter(post_id=post_id)

class CommentsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentsSerializers
