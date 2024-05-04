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
                    "data": serialize_the_data.error,
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
            raise APIException("Internal server error occurred!") from e


@api_view(http_method_names=["GET"])
def get_single_post(request: Request, post_id: int):
    post = get_object_or_404(Post, pk=post_id)
    serializer = PostSerializer(instance=post)
    res = {"message": "singlePost", "data": serializer.data}
    return Response(data=res, status=status.HTTP_200_OK)


@api_view(http_method_names=["PATCH"])
def update(request: Request, post_id: int):
    post = get_object_or_404(Post, pk=post_id)
    data = request.data
    serializer = PostSerializer(instance=post, data=data)
    if serializer.is_valid():
        serializer.save()
        res = {
            "message": "Post updated successfully",
            "success": True,
            "status": status.HTTP_200_OK,
            "data": serializer.data,
        }
        return Response(data=res, status=status.HTTP_200_OK)
    else:
        res = {
            "message": "Post not found",
            "success": True,
            "status": 204,
            "data": "",
        }


@api_view(http_method_names=["DELETE"])
def delete(request: Request, post_id: int):
    post = get_object_or_404(Post, pk=post_id)
    try:
        post.delete()
        res = {
            "message": "Post deleted successfully",
            "success": True,
            "status": status.HTTP_200_OK,
            "data": "",
        }
        return Response(data=res, status=status.HTTP_200_OK)
    except:
        res = {
            "message": "Post not found",
            "success": True,
            "status": 204,
            "data": "",
        }
        return Response(data=res, status=status.HTTP_204_NO_CONTENT)
