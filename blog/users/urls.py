from django.urls import path

from . import views

urlpatterns = [
    path('sign-up', views.sign_up, name='sign-up'),
    path('sign-in', views.sign_in, name='sign-in'),
    path('log-out', views.log_out, name='log-out'),
    path('change-password', views.change_password, name='change-password'),
    path('reset-password', views.reset_password, name='reset-password'),
    path('notification/<str:message>', views.notification_view, name='notification'),
    path('activate/<str:uidb64>/<str:token>', views.activate, name='activate')
]