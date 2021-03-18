from django.urls import include, path, re_path
from rest_framework.routers import DefaultRouter

from .views import UserViewSet, BlogViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'blogs', BlogViewSet, basename="blog")
router.register(r'users', UserViewSet, basename="User")



# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    re_path(r'^', include(router.urls))
]