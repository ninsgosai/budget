from django.urls import path
from . import views

urlpatterns = [
    path('', views.actualexpenses, name='actualexpenses'),
    path('add_actualexpenses/<str:month>', views.add_actualexpenses, name='add_actualexpenses'),
    path('inertexpense', views.inertexpense, name='inertexpense'),
    path('view_expense/<str:month>', views.view_expense, name='view_expense'),
    path('deleteexpense', views.deleteexpense, name='deleteexpense'),
    path('getcategory', views.getcategory, name='getcategory'),
    path('getsubcategory', views.getsubcategory, name='getsubcategory'),

]