from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status, generics, mixins
from rest_framework.decorators import APIView
from rest_framework.exceptions import APIException
from django.http import HttpResponse
from posts.models import Post
from posts.serializers import PostSerializer
from django.shortcuts import get_object_or_404


# GET & POST method to get and post data.
class Create_and_Get_Posts_View(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    # List all the posts
    def get(self, request: Request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    # Create the post
    def post(self, request: Request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# TODO: write this later


class Retrieve_Update_Delete_View(
    generics.GenericAPIView,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    # Get Single Post
    def get(self, request: Request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request: Request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request: Request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
