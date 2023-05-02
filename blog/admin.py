from django.contrib import admin
from .models import Post, Comment

admin.site.register(Post)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('Autor', 'Comentário', 'post', 'created_date', 'approved_comment')
    list_filter = ('approved_comment', 'created_date')
    search_fields = ('Autor', 'Comentário')