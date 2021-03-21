from django.urls import path
from . import views

urlpatterns = [
    path('', views.subadminauth, name='subadminauth'),
    path('subadminlogout', views.subadminlogout, name='subadminlogout'),
]






