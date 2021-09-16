from django.db import models
from uuid import uuid4
from django.utils.timezone import now

# Create your models here.
class Blog(models.Model):

    guid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.TextField(max_length=200,null=False,blank=False)
    content = models.TextField(max_length=20000,null=False,blank=False)
    published = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class meta:
        verbose_name_plural = "Blog Entries"
        ordering = ("-updated",)