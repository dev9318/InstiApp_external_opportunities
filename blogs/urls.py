from .feeds import BlogFeed
from django.urls import path

urlpatterns = [
    path("feed", BlogFeed(), name="feed")
]
