from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:blog_id>/', views.retrieve_blog, name='retrieve_blog'),
]