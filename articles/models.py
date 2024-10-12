from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    contents = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)