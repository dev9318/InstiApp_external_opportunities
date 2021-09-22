from django.contrib.syndication.views import Feed 
from django.urls import reverse_lazy

from .models import Blog, body

class BlogFeed(Feed):
    title = "Blogs added today"
    link = '/blog/feed/'
    description = "RSS feed of the blogs"

    def items(self):
        return Blog.objects.all()

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