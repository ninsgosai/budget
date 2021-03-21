from django.urls import path
from . import views

urlpatterns = [
    path('', views.admintaxcategory, name='admintaxcategory'),
    path('addtaxcategory', views.addtaxcategory, name='addtaxcategory'),
    path('delete_tax_category', views.delete_tax_category, name='delete_tax_category'),
    path('edittax_category', views.edittax_category, name='edittax_category'),
    path('updatetaxcategory', views.updatetaxcategory, name='updatetaxcategory'),
    
    # GOALS
    path('addgoal', views.addgoal, name='addgoal'),

]






