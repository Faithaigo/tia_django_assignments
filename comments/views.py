from rest_framework import generics
from .models import Comment
from .serializers import CommentsSerializers
from rest_framework.permissions import IsAuthenticated


class PostCommentsView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CommentsSerializers

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        return Comment.objects.filter(post_id=post_id)

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_id')
        serializer.save(author=self.request.user, post_id=post_id)

class CommentsView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentsSerializers



