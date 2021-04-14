from rest_framework.generics import ListAPIView, RetrieveAPIView

from posts.models import Post
from .serializers import PostSerializer

# Create your views here.
class PostList(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class SinglePost(RetrieveAPIView):
    lookup_field = 'id'
    queryset = Post.objects.all()
    serializer_class = PostSerializer