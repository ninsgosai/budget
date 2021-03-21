from django.urls import path
from . import views

urlpatterns = [
    #master category
    path('', views.adminbudgetcategories, name='adminbudgetcategories'),
    path('addcategories', views.addcategories, name='addcategories'),
    path('delete_master_category', views.delete_master_category, name='delete_master_category'),
    path('edit_master_category', views.edit_master_category, name='edit_master_category'),
    path('update_master_categories', views.update_master_categories, name='update_master_categories'),
    #category
    path('category', views.category, name='category'),
    path('add_categories', views.add_categories, name='add_categories'),
    path('delete_category', views.delete_category, name='delete_category'),
    path('edit_category', views.edit_category, name='edit_category'),
    path('update_category', views.update_category, name='update_category'),
    #subcategory
    path('subcategory', views.subcategory, name='subcategory'),
    path('add_subcategories', views.add_subcategories, name='add_subcategories'),
    path('delete_subcategory', views.delete_subcategory, name='delete_subcategory'),
    path('edit_subcategory', views.edit_subcategory, name='edit_subcategory'),
    path('update_subcategory', views.update_subcategory, name='update_subcategory'),
]


