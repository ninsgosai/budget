from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
import os

from adminauth.middlewares import checkadminauth
from adminsavingcategory.models import SavingcategoryModel,IncomecategoryModel
from adminusers.models import AdminuserModel

@checkadminauth
def adminsavingcategory(request):
    savingcategory=SavingcategoryModel.objects.all()
    data={'saving_category_page':'active','savingcategory':savingcategory}
    return render(request,'admin_template/saving_category/saving_category.html',data)

@checkadminauth
def addsavingcategory(request):
    if request.method=='POST':
        SavingcategoryModel.objects.create(
            saving_category_name=request.POST['saving_category_name']
        )
        messages.add_message(request, messages.SUCCESS, 'saving category inserted successfully')
        return redirect('adminsavingcategory')
    else:
        data={'saving_category_page':'active'}
        return render(request,'admin_template/saving_category/add_saving_category.html',data)

def delete_saving_category(request):
    if request.method=='POST':
        saving_catid=request.POST['saving_catid']
        data=SavingcategoryModel.objects.get(id=saving_catid)
        data.delete()
        messages.add_message(request, messages.SUCCESS, 'saving category deleted successfully')
        return redirect('adminsavingcategory')

@checkadminauth
def editsavingcategory(request):
    if request.method=='POST':
        save_id=request.POST['save_id']
        savingcat=SavingcategoryModel.objects.get(id=save_id)
        data = {'saving_category_page': 'active','savingcat':savingcat}
        return render(request, 'admin_template/saving_category/edit_saving_category.html', data)

def updatesaving_category(request):
    if request.method=='POST':
        saving_category_ids=request.POST['saving_category_ids']
        data=SavingcategoryModel.objects.get(id=saving_category_ids)
        data.saving_category_name=request.POST['saving_category_name']
        data.save()
        messages.add_message(request, messages.SUCCESS, 'saving category updated successfully')
        return redirect('adminsavingcategory')

def update_income_category(request):
    if request.method == 'POST':
        incomecategory = IncomecategoryModel.objects.get(pk=request.POST['saving_category_ids'])
        incomecategory.income_category_name = request.POST['saving_category_name']
        incomecategory.save()
        incomecategory = IncomecategoryModel.objects.all()  
        messages.add_message(request, messages.SUCCESS, 'income category Updated successfully')
        return render(request,'admin_template/income_category/income_category.html',{'incomecategory':incomecategory})

def incomecategory(request):
    incomecategory = IncomecategoryModel.objects.all()
    return render(request,'admin_template/income_category/income_category.html',{'incomecategory':incomecategory})

def addincomecategory(request):
    if request.method == "POST":
        incomecategory = IncomecategoryModel()
        incomecategory.income_category_name = request.POST['saving_category_name']
        admin = AdminuserModel.objects.get(id=1)
        incomecategory.admin = admin
        incomecategory.save()
        incomecategory = IncomecategoryModel.objects.all()  
        messages.add_message(request, messages.SUCCESS, 'income category Added successfully')

        return render(request,'admin_template/income_category/income_category.html',{'incomecategory':incomecategory})
        
    return render(request,'admin_template/income_category/add_income_category.html')

def editincomecategory(request):
    incomecategory = IncomecategoryModel.objects.get(pk=request.POST['save_id'])
    return render(request,'admin_template/income_category/edit_income_category.html',{'incomecategory':incomecategory})

def delete_income_category(request):
    if request.method=="POST":
        incomecategory = IncomecategoryModel.objects.get(pk=request.POST['saving_catid'])
        incomecategory.delete()
        messages.add_message(request, messages.SUCCESS, 'income category Deleted successfully')
        incomecategory = IncomecategoryModel.objects.all()

    return redirect(incomecategory)













