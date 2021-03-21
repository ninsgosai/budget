from django.urls import path
from . import views

urlpatterns = [
    path('', views.authentication, name='authentication'),
    path('userlogout', views.userlogout, name='userlogout'),
]






