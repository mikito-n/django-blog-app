from atexit import register
from django.contrib import admin
from blog.models import Post, Category, Tag, Comment, Reply
from markdownx.admin import MarkdownxModelAdmin

class PostAdmin(MarkdownxModelAdmin,admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'updated_at', 'is_published')
    search_fields = ('title', 'content')
    list_filter = ('category',)


class ReplyInline(admin.StackedInline):
    model = Reply

class CommentAdmin(admin.ModelAdmin):
    inlines = [ReplyInline]


# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Reply)