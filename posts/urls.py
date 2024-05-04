from django.urls import path
from posts.views import homepage, list_posts, post_detail


urlpatterns = [
    path("home/", homepage, name="posts_home"),
    path("posts_list/", list_posts, name="list_posts"),
    path("<int:index>", post_detail, name="post_detail"),
]
