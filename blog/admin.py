from django.contrib import admin

from .models import TeaBlog, TeaPost, Comment


@admin.register(TeaBlog)
class TeaBlogAdmin(admin.ModelAdmin):
    list_display = ["title", "owner", "is_public"]
    list_display_link = ["title", "owner"]

    
@admin.register(TeaPost)
class TeaPostAdmin(admin.ModelAdmin):
    list_display = ["posted_blog", "post_title"]
    list_display_link = ["posted_blog", "post_title"]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["post", "writer", "comment_body"]
    list_display_link = ["post", "writer", "comment_body"]


# @admin.register()
# class Admin(admin.ModelAdmin):
#     list_display = [""]
#     list_display_link = [""]