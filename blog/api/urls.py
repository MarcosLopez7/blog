from django.urls import path

from . import views

urlpatterns = [
    path('posts', views.PostList.as_view(), name='posts'),
    path('post/<int:id>', views.SinglePost.as_view(), name='get'),
    path('user-posts/<int:user_id>', views.UserPostList.as_view(), name='user-posts')
]