from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArticleView, TagsView, CategoryView

urlpatterns = [
    # TagView
    path('tags/', TagsView.as_view({'get': 'list', 'post': 'create'}), name='Tags-list'),
    path('tags/<int:id>/', TagsView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='Tag-detail'),
    
    # CategoryView
    path('categories/', CategoryView.as_view({'get': 'list', 'post': 'create'}), name='Category-list'),
    path('categories/<int:id>/', CategoryView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='Category-detail'),
    
    # ArticleView
    path('articles/', ArticleView.as_view({'get': 'list', 'post': 'create'}), name='Article-list'),
    path('articles/<int:id>/', ArticleView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='Article-detail'),
]