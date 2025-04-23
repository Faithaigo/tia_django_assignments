from django.db import models
from posts.models import Post
from users.models import User

# Create your models here.
class Comments(models.Model):
    comment = models.TextField()
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="posts")
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="users")