from django.contrib import admin
from .models import Post, PostParagraph


class PostParagraphTabular(admin.TabularInline):
    model = PostParagraph
    extra = 0


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostParagraphTabular]
    list_display = ['title', 'likes_number']