
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(max_length=30, unique=True)




class Tag(models.Model):
    name = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(max_length=30, unique=True)




class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    slug = models.SlugField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='posts')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    tags = models.ManyToManyField(Tag, related_name='posts')

