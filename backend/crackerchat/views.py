from rest_framework import mixins, viewsets

from .models import Post
from .serializers import PostSerializer

class PostViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Post.objects.all()
    serializer_class = PostSerializer