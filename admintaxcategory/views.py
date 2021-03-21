from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
import os

from adminauth.middlewares import checkadminauth
from admintaxcategory.models import TaxcategoryModel
from .models import Goal
from adminusers.models import AdminuserModel

@checkadminauth
def admintaxcategory(request):
    alltaxcategory=TaxcategoryModel.objects.all()
    data={'tax_category_page':'active','alltaxcategory':alltaxcategory}
    return render(request,'admin_template/tax_category/tax_category.html',data)

@checkadminauth
def addtaxcategory(request):
    if request.method=='POST':
        TaxcategoryModel.objects.create(
            tax_category_name=str(request.POST['tax_category_name']).upper()
        )
        messages.add_message(request, messages.SUCCESS, 'tax category inserted successfully')
        return redirect('admintaxcategory')
    else:
        data={'tax_category_page':'active'}
        return render(request,'admin_template/tax_category/add_taxcategory.html',data)

def delete_tax_category(request):
    if request.method=='POST':
        tax_category_id=request.POST['tax_category_id']
        data=TaxcategoryModel.objects.get(id=tax_category_id)
        data.delete()
        messages.add_message(request, messages.SUCCESS, 'tax category deleted successfully')
        return redirect('admintaxcategory')

@checkadminauth
def edittax_category(request):
    if request.method=='POST':
        tax_categories_id=request.POST['tax_categories_id']
        taxcatdata=TaxcategoryModel.objects.get(id=tax_categories_id)
        data = {'tax_category_page': 'active','taxcatdata':taxcatdata}
        return render(request, 'admin_template/tax_category/edit_taxcategory.html', data)


def updatetaxcategory(request):
    if request.method=='POST':
        data=TaxcategoryModel.objects.get(id=request.POST['tax_id'])
        data.tax_category_name=request.POST['tax_category_name']
        data.save()
        messages.add_message(request, messages.SUCCESS, 'tax category updated successfully')
        return redirect('admintaxcategory')

def addgoal(request):
    if request.method == "POST":
        goal = Goal()
        admin = AdminuserModel.objects.get(pk=request.session['user_id'])
        goal.admin = admin
        goal.goal = request.POST['goal']
        goal.goal_amount = request.POST['goal_amount']
        goal.start_date = request.POST['start_date']
        goal.deadline_date = request.POST['end_date']
        goal.status = True
        goal.month = request.POST['month_names']
        goal.save()
        messages.add_message(request, messages.SUCCESS, 'Goal Added successfully')

    return redirect('add_monthlyexpenses',request.POST['month_names'])











