from django.db import models
from uuid import uuid4


# Create your models here.
class Blog(models.Model):

    guid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.TextField(max_length=200, null=False, blank=False)
    content = models.TextField(max_length=20000, null=False, blank=False)
    published = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    body = models.ForeignKey('body', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class meta:
        indexes = [
            models.Index(fields=['title', ]),
        ]
        verbose_name = "Blog Entry"
        verbose_name_plural = "Blog Entries"
        ordering = ("-updated",)


class body(models.Model):

    body_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.TextField(max_length=60)

    def __str__(self):
        return self.name

    class meta:
        indexes = [
            models.Index(fields=['name', ]),
        ]
        verbose_name = "Body Entry"
        verbose_name_plural = "Body Entries"
        ordering = ("name",)
