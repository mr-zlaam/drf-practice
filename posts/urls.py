from django.urls import path
from posts.views import (
    Create_and_Get_Posts_View,
    Retrieve_Update_Delete_View,
)


urlpatterns = [
    path(
        "create_and_get_post/", Create_and_Get_Posts_View.as_view(), name="post_&_get"
    ),
    path(
        "retrieve_update_delete/<int:post_id>",
        Retrieve_Update_Delete_View.as_view(),
        name="get_&_patch_&_delete",
    ),
]
