from django.urls import path
from . import views

urlpatterns = [
    path('', views.subadmindashboard, name='subadmindashboard'),
    #password change
    path('checkuserpassword', views.checkuserpassword, name='checkuserpassword'),
    path('updateuserpassword', views.updateuserpassword, name='updateuserpassword'),
    #profile
    path('subadminprofile', views.subadminprofile, name='subadminprofile'),
    path('updatesubadminprofile', views.updatesubadminprofile, name='updatesubadminprofile'),
]






