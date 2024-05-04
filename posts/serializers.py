from rest_framework.serializers import ModelSerializer
from posts.models import Post

"""
class PostSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=50)
    content = serializers.CharField()
    createdAT = serializers.DateTimeField(read_only=True)

"""


class PostSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = ["id", "title", "content", "createdAT"]
