from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.get_blogs, name='list'),
    path('create-blog/', views.create_blog, name='create_blog'),
    path('<int:blog_id>/', views.retrieve_blog, name='retrieve_blog'),
]