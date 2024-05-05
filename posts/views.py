from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.request import Request
from posts.models import Post
from posts.serializers import PostSerializer

# create your view set


class PostViewSet(viewsets.ViewSet):
    def list(self, request: Request):
        queryset = Post.objects.all()
        serializers = PostSerializer(instance=queryset, many=True)
        return Response(data=serializers.data, status=status.HTTP_200_OK)

    def retrieve(self, request: Request, pk: int):
        post = get_object_or_404(Post, pk=pk)
        serializer = PostSerializer(instance=post)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
