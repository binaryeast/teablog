from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class TimeStampModel(models.Model):
    class Meta:
        abstract = True

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class TeaBlog(models.Model):
    title = models.CharField(max_length=500)
    owner = models.ForeignKey(User, verbose_name="개최자", on_delete=models.CASCADE)
    open_status = [
            ("PUB", "Public"),
            ("PRV", "Private")
            ]
    is_public = models.CharField(
            "공개 상태",
            max_length = 3,
            choices = open_status,
            default = open_status[0][0]
            )


class TeaPost(TimeStampModel):
    posted_blog = models.ForeignKey(TeaBlog, verbose_name="포스트된 블로그", on_delete=models.CASCADE)
    post_title = models.CharField("포스트 제목", max_length=500)
    post_body = models.TextField()

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
