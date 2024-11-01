from django.contrib import admin

from .models import Post, Comment


class CommentAdminInLine(admin.TabularInline):
    model = Comment
    fields = ['text', ]
    extra = 0


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'is_enable', 'publish_date', 'create_data']
    inlines = [CommentAdminInLine, ]

# class CommentAdmin(admin.ModelAdmin):
#    list_display = ['post', 'text', 'create_data']


# admin.site.register(Post, PostAdmin)
# admin.site.register(Comment, CommentAdmin)
