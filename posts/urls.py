from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, TagsViewSet, PostsViewSet

router = DefaultRouter()

router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'tags', TagsViewSet, basename='tag')
router.register(r'', PostsViewSet, basename='post')

urlpatterns = [
    path('', include(router.urls)),
]