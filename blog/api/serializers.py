from django.contrib.auth.models import User

from posts.models import Post

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'image', 'content', 'description', 'user']


class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'image', 'content', 'date', 'description', 'visible', 'user']


class PostEditSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)

    class Meta:
        model = Post
        fields = ['title', 'image', 'content', 'description']


class PostVisibleEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['visible']


class CreateUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def create(self, validated_data):

        return User.objects.create(**validated_data)
