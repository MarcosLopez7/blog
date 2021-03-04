from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.get_posts, name='list'),
    path('add/', views.add_post, name='add'),
    path('edit/<int:post_id>/', views.edit_post, name='edit'), 
    path('delete/<int:post_id>/', views.delete_post, name='delete'),
    path('<int:post_id>/', views.get_post, name='get'),
]