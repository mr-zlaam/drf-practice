from django.urls import path
from posts.views import homepage, list_posts


urlpatterns = [
    path("home/", homepage, name="posts_home"),
    path("posts_list/", list_posts, name="list_posts"),
]
