from django.urls import path
from .views import PostsView, PostView


urlpatterns = [
    path('', PostsView.as_view()),
    path('<int:pk>/details', PostView.as_view())
]