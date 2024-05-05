from django.urls import include, path
from rest_framework.routers import DefaultRouter
from posts.views import PostViewSet

router = DefaultRouter()
router.register("hero/", PostViewSet, basename="posts")
urlpatterns = [
    path("posts/", include(router.urls)),
]
