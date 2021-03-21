from django.urls import path
from . import views

urlpatterns = [
    path('', views.subadminusers, name='subadminusers'),
    path('add_users', views.add_users, name='add_users'),
    path('delete_subadminusers', views.delete_subadminusers, name='delete_subadminusers'),
    path('edit_subadminusers', views.edit_subadminusers, name='edit_subadminusers'),
    path('update_subadminusers', views.update_subadminusers, name='update_subadminusers'),
    path('subadmin_view_estimate_expanse/<int:id>', views.subadmin_view_estimate_expanse, name='subadmin_view_estimate_expanse'),
    path('subadmin_monthwise_estimate', views.subadmin_monthwise_estimate, name='subadmin_monthwise_estimate'),
]






