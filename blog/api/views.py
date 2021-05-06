from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView
from rest_framework.response import Response

from posts.models import Post
from .serializers import PostSerializer, PostCreateSerializer, PostEditSerializer, PostVisibleEditSerializer


class PostList(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostCreateView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer


class UserPostList(ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def list(self, request, user_id):
        queryset = Post.objects.filter(user__pk=user_id)
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)


class SinglePost(RetrieveAPIView):
    lookup_field = 'id'
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostEdit(UpdateAPIView):
    lookup_field = 'id'
    queryset = Post.objects.all()
    serializer_class = PostEditSerializer


class PostEditVisible(UpdateAPIView):
    lookup_field = 'id'
    queryset = Post.objects.all()
    serializer_class = PostVisibleEditSerializer
