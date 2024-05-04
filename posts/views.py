from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.http import HttpResponse
from posts.models import Post
from posts.serializers import PostSerializer
from django.shortcuts import get_object_or_404

# Create your views here.;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
posts = [
    {"id": 1, "name": "John Doe", "age": 30},
    {"id": 2, "name": "Jane Smith", "age": 25},
    {"id": 3, "name": "Bob Johnson", "age": 40},
    {"id": 4, "name": "Alice Brown", "age": 28},
    {"id": 5, "name": "Mike Davis", "age": 35},
    {"id": 6, "name": "Emily Taylor", "age": 22},
    {"id": 7, "name": "Sarah Lee", "age": 32},
    {"id": 8, "name": "Kevin White", "age": 45},
    {"id": 9, "name": "Lisa Hall", "age": 38},
    {"id": 10, "name": "Tom Harris", "age": 42},
]


@api_view(http_method_names=["POST", "GET"])
def homepage(request: Request):
    if request.method == "POST":
        data = request.data
        res = {
            "message": "OK",
            "success": True,
            "status": status.HTTP_201_CREATED,
            "data": data,
        }
        return Response(data=res, status=status.HTTP_201_CREATED)
    return HttpResponse("Hello world")


@api_view(http_method_names=["GET", "POST"])
def list_posts(request: Request):
    posts = Post.objects.all()
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
    serializers = PostSerializer(instance=posts, many=True)
    response = {
        "message": "posts",
        "success": True,
        "status": 200,
        "data": serializers.data,
    }
    return Response(data=response, status=status.HTTP_200_OK)


@api_view(http_method_names=["GET"])
def post_detail(request: Request, post_id: int):

    post = get_object_or_404(Post, pk=post_id)
    serializer = PostSerializer(instance=post)
    res = {"message": "singlePost", "data": serializer.data}
    return Response(data=res, status=status.HTTP_200_OK)
