from django.urls import path

from . import views

urlpatterns = [
    path('sign-up/', views.sign_up, name='sign-up'),
    path('successful/', views.successful_registration, name='successful')
]