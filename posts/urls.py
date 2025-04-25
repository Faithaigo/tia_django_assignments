from django.urls import path
from .views import Categories, CategoryDetail, Tags, TagDetails, Posts, PostDetails

urlpatterns = [
    path('category', Categories.as_view()),
    path('category/<int:pk>', CategoryDetail.as_view()),
    path('tag', Tags.as_view()),
    path('tag/<int:pk>', TagDetails.as_view()),
    path('', Posts.as_view()),
    path('<int:pk>', PostDetails.as_view())
]