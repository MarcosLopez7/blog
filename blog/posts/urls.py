from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.get_posts, name='list'),
    path('add/', views.add_post, name='add_post'),
    path('<int:post_id>/', views.get_post, name='get_post'),
]