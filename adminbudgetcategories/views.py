from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib import messages
import os

from adminauth.middlewares import checkadminauth
from adminbudgetcategories.models import BudgetcategoriesModel,BudgetsubcategoriesModel,BudgetlastcategoriesModel

#master category functions
@checkadminauth
def adminbudgetcategories(request):
    category=BudgetcategoriesModel.objects.all()
    data={'budget_category_page':'active','category':category}
    return render(request,'admin_template/budget_mastercategories/category.html',data)

@checkadminauth
def addcategories(request):
    if request.method=='POST':
        BudgetcategoriesModel.objects.create(
            category_name=str(request.POST['category_name']).upper()
        )
        messages.add_message(request, messages.SUCCESS, 'master category inserted successfully')
        return redirect('adminbudgetcategories')
    else:
        data = {'budget_category_page': 'active'}
        return render(request, 'admin_template/budget_mastercategories/add_categories.html', data)

def delete_master_category(request):
    if request.method=='POST':
        data=BudgetcategoriesModel.objects.get(id=request.POST['mastercategory_id'])
        data.delete()
        messages.add_message(request, messages.SUCCESS, 'master category deleted successfully')
        return redirect('adminbudgetcategories')

@checkadminauth
def edit_master_category(request):
    if request.method=='POST':
        m_category_id=request.POST['m_category_id']
        master_category=BudgetcategoriesModel.objects.get(id=m_category_id)
        data = {'budget_category_page': 'active','master_category':master_category}
        return render(request, 'admin_template/budget_mastercategories/edit_categories.html', data)

def update_master_categories(request):
    if request.method=='POST':
        master_hidden_id=request.POST['master_hidden_id']
        data=BudgetcategoriesModel.objects.get(id=master_hidden_id)
        data.category_name=str(request.POST['category_name']).upper()
        data.save()
        messages.add_message(request, messages.SUCCESS, 'master category updated successfully')
        return redirect('adminbudgetcategories')

#for category
@checkadminauth
def category(request):
    allcategory=BudgetsubcategoriesModel.objects.all().values()
    for newallcategory in allcategory:
        getmastercat=BudgetcategoriesModel.objects.get(id=newallcategory['budget_category_id'])
        newallcategory['master_category_name']=str(getmastercat.category_name).upper()
    data={'budget_category_page':'active','allcategory':allcategory}
    return render(request,'admin_template/budget_category/category.html',data)

@checkadminauth
def add_categories(request):
    if request.method=='POST':
        BudgetsubcategoriesModel.objects.create(
            budget_category_id=request.POST['budget_category_id'],
            subcategory_name=str(request.POST['subcategory_name']).upper()
        )
        messages.add_message(request, messages.SUCCESS, 'category inserted successfully')
        return redirect('category')
    else:
        mastercategory=BudgetcategoriesModel.objects.all()
        data = {'budget_category_page': 'active','mastercategory':mastercategory}
        return render(request, 'admin_template/budget_category/add_category.html', data)

def delete_category(request):
    if request.method=='POST':
        category_id=request.POST['category_id']
        data=BudgetsubcategoriesModel.objects.get(id=category_id)
        data.delete()
        messages.add_message(request, messages.SUCCESS, 'category deleted successfully')
        return redirect('category')

@checkadminauth
def edit_category(request):
    if request.method=='POST':
        cat_id=request.POST['cat_id']
        categorydata=BudgetsubcategoriesModel.objects.get(id=cat_id)
        mastercategory = BudgetcategoriesModel.objects.all()
        data = {'budget_category_page': 'active', 'categorydata': categorydata,'mastercategory':mastercategory}
        return render(request, 'admin_template/budget_category/edit_categories.html', data)

def update_category(request):
    if request.method=='POST':
        category_ids=request.POST['category_ids']
        data=BudgetsubcategoriesModel.objects.get(id=category_ids)
        data.budget_category_id=request.POST['budget_category_id']
        data.subcategory_name=str(request.POST['subcategory_name']).upper()
        data.save()
        messages.add_message(request, messages.SUCCESS, 'category updated successfully')
        return redirect('category')


#Subcategory functions
@checkadminauth
def subcategory(request):
    allsubcategory=BudgetlastcategoriesModel.objects.all().values()
    for newallsubcategory in allsubcategory:
         getcategoryname=BudgetsubcategoriesModel.objects.get(id=newallsubcategory['budget_subcategory_id'])
         newallsubcategory['category_name']=str(getcategoryname.subcategory_name).upper()
    data={'budget_category_page':'active','allsubcategory':allsubcategory}
    return render(request,'admin_template/budget_subcategories/subcategory.html',data)

@checkadminauth
def add_subcategories(request):
    if request.method=='POST':
        BudgetlastcategoriesModel.objects.create(
            budget_subcategory_id=request.POST['budget_subcategory_id'],
            last_category_name=str(request.POST['last_category_name']).upper()
        )
        messages.add_message(request, messages.SUCCESS, 'subcategory inserted successfully')
        return redirect('subcategory')
    else:
        categorys=BudgetsubcategoriesModel.objects.all()
        data = {'budget_category_page': 'active','categorys':categorys}
        return render(request, 'admin_template/budget_subcategories/add_subcategory.html', data)


def delete_subcategory(request):
    if request.method=='POST':
        subcat_id=request.POST['subcat_id']
        data=BudgetlastcategoriesModel.objects.get(id=subcat_id)
        data.delete()
        messages.add_message(request, messages.SUCCESS, 'subcategory deleted successfully')
        return redirect('subcategory')

@checkadminauth
def edit_subcategory(request):
    if request.method=='POST':
        subcategory_ids=request.POST['subcategory_ids']
        subcategorydata=BudgetlastcategoriesModel.objects.get(id=subcategory_ids)
        categorys = BudgetsubcategoriesModel.objects.all()
        data = {'budget_category_page': 'active', 'categorys': categorys,'subcategorydata':subcategorydata}
        return render(request, 'admin_template/budget_subcategories/edit_subcategories.html', data)


def update_subcategory(request):
    if request.method=='POST':
        subcatids=request.POST['subcatids']
        data=BudgetlastcategoriesModel.objects.get(id=subcatids)
        data.budget_subcategory_id=request.POST['budget_subcategory_id']
        data.last_category_name=str(request.POST['last_category_name']).upper()
        data.save()
        messages.add_message(request, messages.SUCCESS, 'subcategory updated successfully')
        return redirect('subcategory')










