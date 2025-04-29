from django.db import models
from posts.models import Post

# Create your models here.
class Comment(models.Model):
    comment = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
