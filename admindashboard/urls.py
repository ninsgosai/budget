from django.urls import path
from . import views

urlpatterns = [
    path('', views.admindashboard, name='admindashboard'),
    path('checkpassword', views.checkpassword, name='checkpassword'),
    path('updatepassword', views.updatepassword, name='updatepassword'),
    path('adminprofile', views.adminprofile, name='adminprofile'),
]






