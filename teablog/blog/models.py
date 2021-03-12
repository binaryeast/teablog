from django.db import models
from django.contrib.auth import get_user_model

from model_utils.models import TimeStampedModel
from datetime import timedelta

User = get_user_model()

class Blog(models.Model):
    """
    User's blog.

    One user can make several blogs.

    It has mainpage, posts, posts' comment.
    """
    class Meta:
        verbose_name = "블로그"
        verbose_name_plural = verbose_name

    blog_name = models.CharField("블로그 이름", max_length=500)
    owner = models.ForeignKey(User, verbose_name="블로그 주인", on_delete=models.CASCADE)


    def __str__(self):
        return self.blog_name


class Post(TimeStampedModel):
    """
    Blog post.

    It has comments.
    """
    class Meta:
        verbose_name = "포스트"
        verbose_name_plural = verbose_name

    blog = models.ForeignKey(Blog, verbose_name="블로그", null=True, on_delete=models.SET_NULL)
    post_name = models.CharField("포스트 이름", max_length=500) 
    post_body = models.TextField()

    def __str__(self):
        return self.post_name


class Comment(TimeStampedModel):
    """
    Blog post's comment.

    It has time(created and modified), user, post foreignkey.
    """
    class Meta:
        verbose_name = "댓글"
        verbose_name_plural = verbose_name

    post = models.ForeignKey(Post, verbose_name="달린 포스트", on_delete=models.CASCADE)
    writer = models.ForeignKey(User, verbose_name="댓쓴이", null=True, on_delete=models.SET_NULL)
    comment_body = models.TextField("댓글") 

    def __str__(self):
        return self.post_name
