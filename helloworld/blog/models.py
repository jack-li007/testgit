from django.db import models
class Article(models.Model):
    title = models.CharField(max_length = 100)
    author = models.CharField(max_length = 30)
    body = models.TextField()
    timestamp = models.DateTimeField()

# Create your models here.
