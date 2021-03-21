from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('checkuserpassword', views.checkuserpassword, name='checkuserpassword'),
    path('updateuserpassword', views.updateuserpassword, name='updateuserpassword'),
    path('userprofile', views.userprofile, name='userprofile'),
    path('updateprofile', views.updateprofile, name='updateprofile'),
]






