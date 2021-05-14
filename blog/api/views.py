from django.conf import settings
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string

from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from users.tokens import account_activation_token
from posts.models import Post

from .serializers import (
    PostSerializer,
    PostCreateSerializer,
    PostEditSerializer,
    PostVisibleEditSerializer,
    CreateUserSerializer
)


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


class CreateUserAPIView(APIView):

    def post(self, request, format=None):
        serializer = CreateUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.is_active = False
            user.save()

            title = 'Gracias por registrarte'
            content = """
                                Esperemos que los posts de este blog sean de tu agrado.\n\n
                                Por favor da click en el siguiente enlace para que podamos validar tu correo
                            """
            url_site = get_current_site(request)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = account_activation_token.make_token(user),
            message = render_to_string('users/email_validation.html', {
                'user': user,
                'domain': url_site,
                'uid': uid,
                'token': token[0],
                'title': title,
                'content': content,
                'password': None
            })
            send_mail(
                subject='Gracias por registrate al blog',
                message=message,
                from_email=settings.EMAIL_SENDER,
                recipient_list=[user.email],
                fail_silently=False,
                html_message=message,
            )

            return Response(serializer.data, status=status.HTTP_201_CREATED)