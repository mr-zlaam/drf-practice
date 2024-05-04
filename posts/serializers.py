from rest_framework.serializers import ModelSerializer, CharField
from posts.models import Post

"""
class PostSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=50)
    content = serializers.CharField()
    createdAT = serializers.DateTimeField(read_only=True)

"""


class PostSerializer(ModelSerializer):
    title = CharField(max_length=50, min_length=2)

    class Meta:
        model = Post
        fields = ["id", "title", "content", "createdAT"]
