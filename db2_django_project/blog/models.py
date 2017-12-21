from django.db import models
from django.conf import settings
from accounts.models import User

from utils import get_file_path


class Article(models.Model):
    """
    Describes basic article fields.
    """
    title = models.CharField(max_length=200, unique=True)
    title_image = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    body = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    liked_by = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='article_liked_by', blank=True)
    comment = models.ManyToManyField('Comment', related_name='article_comment', blank=True)

    class Meta:
        ordering = ['id']


class Comment(models.Model):
    """
    Describes comment fields.
    Comment to article model.
    """
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comment_author')
    article = models.ManyToManyField(Article, related_name='comment_article')
    body = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        ordering = ['-created_date']
