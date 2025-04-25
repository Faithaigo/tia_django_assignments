from django.urls import path
from .views import Categories, CategoryDetail, Tags, TagDetails

urlpatterns = [
    path('category', Categories.as_view()),
    path('category/<int:pk>', CategoryDetail.as_view()),
    path('tag', Tags.as_view()),
    path('tag/<int:pk>', TagDetails.as_view())
]