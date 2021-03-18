from rest_framework import serializers

from .models import TeaBlog, TeaPost, Comment

from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']
        extra_kwargs = {'url': {'view_name': 'blog:user-detail'}}


# blogs
class TeaBlogSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="Owner.username")
    class Meta:
        model = TeaBlog
        fields = ["title", "owner", "is_public"]
        depth = 1


class TeaPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeaPost
        fields = ["posted_blog", "post_title", "post_body"]



class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="Owner.username")
    class Meta:
        model = Comment
        fields = ["post", "writer", "comment_body"]
        depth = 1
