from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import TeaBlog, TeaPost, Comment
from .serializers import UserSerializer, TeaBlogSerializer, TeaPostSerializer, CommentSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BlogList(APIView):
    def get(self, request, format=None):
        blogs = TeaBlog.objects.all()
        serializer = TeaBlogSerializer(blogs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TeaBlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


