from django.urls import path
from .views import PostCommentsView,CommentsView


urlpatterns = [
    path('posts/<int:post_id>', PostCommentsView.as_view()),
    path('<int:pk>', CommentsView.as_view())
]