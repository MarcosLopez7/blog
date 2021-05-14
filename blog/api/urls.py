from django.urls import path

from . import views

urlpatterns = [
    path('posts', views.PostList.as_view(), name='posts'),
    path('add-post', views.PostCreateView.as_view(), name='add-post'),
    path('sign-up', views.CreateUserAPIView.as_view(), name='sign-up'),
    path('post/<int:id>', views.SinglePost.as_view(), name='get'),
    path('edit-post/<int:id>', views.PostEdit.as_view(), name='edit-post'),
    path('user-posts/<int:user_id>', views.UserPostList.as_view(), name='user-posts'),
    path('edit-visible-post/<int:id>', views.PostEditVisible.as_view(), name='edit-visible-post')
]
