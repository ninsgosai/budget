from django.urls import path
from . import views

urlpatterns = [
    path('', views.monthlyexpenses, name='monthlyexpenses'),
    path('add_monthlyexpenses/<str:month>', views.add_monthlyexpenses, name='add_monthlyexpenses'),
    #for income
    path('insertusserincome', views.insertusserincome, name='insertusserincome'),
    path('deleteincome', views.deleteincome, name='deleteincome'),
    path('editincome', views.editincome, name='editincome'),
    path('updateincome', views.updateincome, name='updateincome'),
    #for tax
    path('inserttax', views.inserttax, name='inserttax'),
    path('deletetax', views.deletetax, name='deletetax'),
    path('edittax', views.edittax, name='edittax'),
    path('updatetax', views.updatetax, name='updatetax'),
    # for savings
    path('insertsavings', views.insertsavings, name='insertsavings'),
    path('deletesavings', views.deletesavings, name='deletesavings'),
    path('editsavings', views.editsavings, name='editsavings'),
    path('updatesavings', views.updatesavings, name='updatesavings'),
    #for expenses
    path('getcategory', views.getcategory, name='getcategory'),
    path('getsubcategory', views.getsubcategory, name='getsubcategory'),
    path('insertexpenses', views.insertexpenses, name='insertexpenses'),
    path('deleteexpenses', views.deleteexpenses, name='deleteexpenses'),
    path('editexpense', views.editexpense, name='editexpense'),
    path('updateexpensedata', views.updateexpensedata, name='updateexpensedata'),

    # FOR GOALS 
    path('editgoal', views.editgoal, name='editgoal'),
    path('updategoal', views.updategoal, name='updategoal'),
    path('delete_goal', views.delete_goal, name='delete_goal'),

#third============================
#income
path('userestimates', views.userestimates, name='userestimates'),
path('savename', views.savename, name='savename'),
path('insertincome', views.insertincome, name='insertincome'),
path('updatename', views.updatename, name='updatename'),

#tax
path('inserttaxname', views.inserttaxname, name='inserttaxname'),
path('updatetaxcategory', views.updatetaxcategory, name='updatetaxcategory'),
path('edittaxper', views.edittaxper, name='edittaxper'),
path('updatemembername', views.updatemembername, name='updatemembername'),

#savings
path('savesavingsname', views.savesavingsname, name='savesavingsname'),
path('insertsavingsper', views.insertsavingsper, name='insertsavingsper'),
path('updatesavingper', views.updatesavingper, name='updatesavingper'),
path('updatesavingname', views.updatesavingname, name='updatesavingname'),
















]
