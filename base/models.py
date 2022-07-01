from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Major(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Topic(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    major = models.ForeignKey(Major, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200)
    body = models.TextField(null=True, blank=True)
    # participants = 
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.title

class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]