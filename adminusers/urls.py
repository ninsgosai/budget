from django.urls import path
from . import views

urlpatterns = [
    #for creating users
    path('', views.adminusers, name='adminusers'),
    path('addusers', views.addusers, name='addusers'),
    path('deleteuser', views.deleteuser, name='deleteuser'),
    path('edituser/<str:pk>', views.edituser, name='edituser'),
    path('updateusers', views.updateusers, name='updateusers'),
    path('view_estimate_expanse/<int:id>', views.view_estimate_expanse, name='view_estimate_expanse'),
    path('monthwise_estimate', views.monthwise_estimate, name='monthwise_estimate'),
    path('editaccount', views.editaccount, name='editaccount'),

    #for creating subadmin
    path('subadmin', views.subadmin, name='subadmin'),
    path('addsubadmin', views.addsubadmin, name='addsubadmin'),
    path('deletesubadmin', views.deletesubadmin, name='deletesubadmin'),
    path('editsubadmin', views.editsubadmin, name='editsubadmin'),
    path('updatesubadmin', views.updatesubadmin, name='updatesubadmin'),
    path('changeStatus', views.changeStatus, name='changeStatus'),
    path('changeSubStatus', views.changeSubStatus, name='changeSubStatus'),

]






