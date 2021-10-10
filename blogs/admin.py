from django.contrib import admin

from django_summernote.admin import SummernoteModelAdmin
from .models import Blog, body

# Apply summernote to all TextField in model.
class BlogAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = ('content',)
    search_fields = ['title','content']

admin.site.register(Blog, BlogAdmin)

class bodyAdmin(admin.ModelAdmin):
    search_fields = ['name']

admin.site.register(body,  bodyAdmin)