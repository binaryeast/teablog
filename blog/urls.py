from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from .views import UserViewSet, BlogList

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'blogs', BlogList, basename="blog")
router.register(r'users', UserViewSet, basename="User")

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    re_path(r'^', include(router.urls))
]