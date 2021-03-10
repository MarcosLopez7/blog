from django.urls import path

from . import views

urlpatterns = [
    path('sign-up/', views.sign_up, name='sign-up'),
    path('sign-in/', views.sign_in, name='sign-in'),
    path('log-out/', views.log_out, name='log-out'),
    path('successful/', views.successful_registration, name='successful'),
    path('activate/<str:uidb64>/<str:token>/', views.activate, name='activate')
]