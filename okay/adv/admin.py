from django.contrib import admin
from .models import Tags, Category, Article

@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    search_fields = ('tag_name',)  # Use 'tag_name' instead of 'tags_name'
    list_display = ('id', 'tag_name')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('category_name',)
    list_display = ('id', 'category_name')

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ('title', 'content', 'publish_date')