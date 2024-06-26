from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, APIView
from rest_framework.exceptions import APIException
from django.http import HttpResponse
from posts.models import Post
from posts.serializers import PostSerializer
from django.shortcuts import get_object_or_404


# GET & POST method to get and post data.
class Create_and_Get_Posts_View(APIView):
    serializer_class = PostSerializer

    # ***Get Request
    def get(self, request: Request, *args, **kwargs):
        try:
            posts = Post.objects.all()
            serialize_the_data = self.serializer_class(instance=posts, many=True)
            response_from_serializers = {
                "message": "OK",
                "success": True,
                "status": status.HTTP_200_OK,
                "data": serialize_the_data.data,
            }
            return Response(data=response_from_serializers, status=status.HTTP_200_OK)

        except Exception as e:
            raise APIException("some thing went wrong while getting posts", e) from e

    # ***Post Request
    def post(self, request: Request, *args, **kwargs):
        data_from_client = request.data
        try:
            if (
                data_from_client.get("title")
                and data_from_client.get("content") is not None
            ):
                serialize_the_data = self.serializer_class(data=data_from_client)
                if serialize_the_data.is_valid():
                    serialize_the_data.save()
                    response_from_serializers = {
                        "message": "post created successfully",
                        "success": True,
                        "status": status.HTTP_201_CREATED,
                        "data": serialize_the_data.data,
                    }
                    return Response(
                        data=response_from_serializers, status=status.HTTP_201_CREATED
                    )
                error_from_serializer = {
                    "message": "some thing went wrong while creating posts",
                    "success": False,
                    "status": status.HTTP_400_BAD_REQUEST,
                    "data": serialize_the_data.errors,
                }
                return Response(
                    data=error_from_serializer, status=status.HTTP_400_BAD_REQUEST
                )
            else:
                error = {
                    "message": "title and content are required",
                    "success": False,
                    "status": status.HTTP_403_FORBIDDEN,
                    "data": None,
                }
                return Response(data=error, status=status.HTTP_403_FORBIDDEN)
        except Exception as e:
            raise APIException("some thing went wrong while creating posts") from e


# TODO: write this later


class Retrieve_Update_Delete_View(APIView):
    serializer_class = PostSerializer

    # Get Single Post
    def get(
        self,
        request: Request,
        post_id: int,
    ):
        try:
            query_single_post = get_object_or_404(Post, pk=post_id)
            serialize_the_single_post = self.serializer_class(
                instance=query_single_post
            )
            response_after_serialization = {
                "message": "OK",
                "success": True,
                "status": status.HTTP_200_OK,
                "data": serialize_the_single_post.data,
            }
            return Response(
                data=response_after_serialization, status=status.HTTP_200_OK
            )
        except Exception as e:
            raise APIException(
                "Internal server error occurred while getting the post"
            ) from e

    # Update Post
    def patch(self, request: Request, post_id: int):
        data_from_client_to_update = request.data
        try:
            query_post_to_update = get_object_or_404(Post, pk=post_id)
            if (
                data_from_client_to_update.get("title")
                and data_from_client_to_update.get("content") is not None
            ):
                serialize_the_data = self.serializer_class(
                    instance=query_post_to_update, data=data_from_client_to_update
                )
                if serialize_the_data.is_valid():
                    serialize_the_data.save()
                    response_after_serialization = {
                        "message": "Post updated successfully",
                        "success": True,
                        "status": status.HTTP_200_OK,
                        "data": serialize_the_data.data,
                    }
                    return Response(
                        data=response_after_serialization,
                        status=status.HTTP_201_CREATED,
                    )
                else:
                    error_from_serializer = {
                        "message": "some thing went wrong while updating post",
                        "success": False,
                        "status": status.HTTP_400_BAD_REQUEST,
                        "data": serialize_the_data.errors,
                    }
                    return Response(
                        data=error_from_serializer, status=status.HTTP_400_BAD_REQUEST
                    )
            else:
                error = {
                    "message": "title and content are required",
                    "success": False,
                    "status": status.HTTP_403_FORBIDDEN,
                    "data": None,
                }
                return Response(data=error, status=status.HTTP_403_FORBIDDEN)
        except Exception as e:
            raise APIException("Internal server error occured while updating") from e

    # Delete Post
    def delete(self, request: Request, post_id: int):
        query_post_to_delete = get_object_or_404(Post, pk=post_id)
        try:
            query_post_to_delete.delete()
            response_after_querying_post_for_delete = {
                "message": "Post deleted successfully",
                "success": True,
                "status": status.HTTP_204_NO_CONTENT,
                "data": "",
            }
            return Response(
                data=response_after_querying_post_for_delete,
                status=status.HTTP_204_NO_CONTENT,
            )
        except Exception as e:
            raise APIException(
                "Internal server error occurred while deleting the post!!!"
            )
