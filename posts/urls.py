from django.urls import path
from posts.views import get_single_post, update, delete, Create_and_Get_Posts_View


urlpatterns = [
    path(
        "create_and_get_post/", Create_and_Get_Posts_View.as_view(), name="post_&_get"
    ),
    path("posts_list/<int:post_id>", get_single_post, name="get_single_post"),
    path("update_post/<int:post_id>/", update, name="update_post"),
    path("delete_post/<int:post_id>/", delete, name="delete_post"),
]
