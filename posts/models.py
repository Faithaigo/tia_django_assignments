from django.db import models
from users.models import User

class Post(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")