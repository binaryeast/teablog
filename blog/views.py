from django.http import Http404
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, renderers, viewsets
from rest_framework.decorators import action

from .models import TeaBlog, TeaPost, Comment
from .serializers import UserSerializer, TeaBlogSerializer, TeaPostSerializer, CommentSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BlogViewSet(viewsets.ModelViewSet):
        queryset = TeaBlog.objects.all()
        serializer_class = TeaBlogSerializer
        permission_classes = (permissions.IsAuthenticatedOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


