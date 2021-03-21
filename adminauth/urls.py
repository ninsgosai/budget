from django.urls import path
from . import views

urlpatterns = [
    path('', views.adminauth, name='adminauth'),
    path('adminlogout', views.adminlogout, name='adminlogout'),
]






