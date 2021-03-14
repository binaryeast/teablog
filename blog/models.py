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

