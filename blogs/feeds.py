from django.contrib.syndication.views import Feed 
from django.urls import reverse_lazy

from .models import Blog, body

from datetime import timedelta
from django.utils import timezone

class BlogFeed(Feed):
    title = "Blogs added today"
    link = '/blog/feed/'
    description = "RSS feed of the blogs"

    def items(self):
        current_time = timezone.now().replace(minute=0, second=0, microsecond=0)
        one_hour_before = current_time - timedelta(hours=1)
        return Blog.objects.filter(updated__range=(one_hour_before,current_time))

    def item_title(self, item):
        return item.title

    def item_guid(self, item):
        return item.guid

    def item_description(self, item):
        return item.content

    def item_pubdate(self, item):
        return item.published

    def item_author_name(self,item):
        return item.body

    def item_link(self, item):
        return ""