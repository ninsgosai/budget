from django.urls import path
from . import views

urlpatterns = [
    path('', views.adminsavingcategory, name='adminsavingcategory'),
    path('addsavingcategory', views.addsavingcategory, name='addsavingcategory'),
    path('delete_saving_category', views.delete_saving_category, name='delete_saving_category'),
    path('editsavingcategory', views.editsavingcategory, name='editsavingcategory'),
    path('updatesaving_category', views.updatesaving_category, name='updatesaving_category'),
    path('update_income_category', views.update_income_category, name='update_income_category'),
    path('incomecategory', views.incomecategory, name='incomecategory'),
    path('addincomecategory', views.addincomecategory, name='addincomecategory'),
    path('editincomecategory', views.editincomecategory, name='editincomecategory'),
    path('delete_income_category', views.delete_income_category, name='delete_income_category'),
]






