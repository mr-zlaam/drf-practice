from django.urls import path
from posts.views import (
    homepage,
    list_posts,
    get_single_post,
    update,
    delete,
    Create_and_Get_Posts,
)


urlpatterns = [
    path("create_post/", homepage, name="posts_home"),
    path("create_and_get_post/", Create_and_Get_Posts.as_view(), name="p/get"),
    path("posts_list/", list_posts, name="list_posts"),
    path("posts_list/<int:post_id>", get_single_post, name="get_single_post"),
    path("update_post/<int:post_id>/", update, name="update_post"),
    path("delete_post/<int:post_id>/", delete, name="delete_post"),
]
