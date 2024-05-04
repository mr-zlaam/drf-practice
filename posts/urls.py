from django.urls import path
from posts.views import homepage, list_posts, get_single_post, update, delete


urlpatterns = [
    path("home/", homepage, name="posts_home"),
    path("posts_list/", list_posts, name="list_posts"),
    path("get_single_post/<int:post_id>", get_single_post, name="get_single_post"),
    path("update/<int:post_id>/", update, name="update_post"),
    path("delete/<int:post_id>/", delete, name="delete_post"),
]
