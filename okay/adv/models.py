from django.db import models
import datetime

class Tags(models.Model):
    tag_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.tag_name

class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.category_name

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    tags = models.ManyToManyField(Tags)
    publish_date = models.DateTimeField(null=True)  # Use datetime.timezone.utc as the default
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title