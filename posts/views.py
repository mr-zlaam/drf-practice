from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.http import HttpResponse
from posts.models import Post
from posts.serializers import PostSerializer
from django.shortcuts import get_object_or_404

# Create your views here.;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;


@api_view(http_method_names=["POST"])
def homepage(request: Request):
    if request.method == "POST":
        data = request.data
        serializers = PostSerializer(data=data)
        if serializers.is_valid():
            serializers.save()
            res = {
                "message": "post created successfully",
                "success": True,
                "status": 201,
                "data": serializers.data,
            }
            return Response(data=res, status=status.HTTP_201_CREATED)
        error = {
            "message": "error while creating post",
            "sucess": False,
            "status": 500,
            "error": serializers.errors,
        }
        return Response(data=error)


@api_view(http_method_names=["GET"])
def list_posts(request: Request):
    posts = Post.objects.all()

    serializers = PostSerializer(instance=posts, many=True)
    response = {
        "message": "All Posts are here",
        "success": True,
        "status": 200,
        "data": serializers.data,
    }
    return Response(data=response, status=status.HTTP_200_OK)


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
