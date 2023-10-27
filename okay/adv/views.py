from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from adv.models import Article, Tags, Category
from rest_framework import status
from .serializers import ArticleSerializer, TagSerializer, CategorySerializer

class ArticleView(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'id'

    def list(self, request):
        articles = self.get_queryset()  # Changed variable name for clarity
        serializer = self.get_serializer(articles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)  # Use status codes as constants

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TagsView(ModelViewSet):
    queryset = Tags.objects.all()
    serializer_class = TagSerializer
    lookup_field = 'id'

    def list(self, request):
        tags = self.get_queryset()  # Changed variable name for clarity
        serializer = self.get_serializer(tags, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Rest of the TagsView methods remain the same

class CategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'id'

    def list(self, request):
        categories = self.get_queryset()  # Changed variable name for clarity
        serializer = self.get_serializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    