from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
import os
import calendar
from datetime import *

from adminauth.middlewares import checkadminauth
from adminusers.models import AdminuserModel,SubadminauthModel,UserincomeCategory
from monthlyexpenses.models import IncomeModel,TaxModel,SavingsModel,ExpensesModel
from admintaxcategory.models import TaxcategoryModel
from adminsavingcategory.models import SavingcategoryModel,IncomecategoryModel
from adminbudgetcategories.models import BudgetcategoriesModel,BudgetsubcategoriesModel,BudgetlastcategoriesModel
from .models import *
#user functions
@checkadminauth
def adminusers(request):
    userdata=AdminuserModel.objects.all()
    data={'adminusser_page':'active','userdata':userdata}
    return render(request,'admin_template/users/users.html',data)

@checkadminauth
def addusers(request):
    if request.method=='POST':
            subscription_from_time = request.POST['subscription_from_time']
            subscription_to_time = request.POST['subscription_to_time']
            date1 = datetime.strptime(subscription_from_time, "%Y-%m-%d")
            date2 = datetime.strptime(subscription_to_time, "%Y-%m-%d")
            date1 = date1.replace(day=1)
            date2 = date2.replace(day=1)
            months_str = calendar.month_name
            months = []
            while date1 < date2:
                month = date1.month
                year = date1.year
                month_str = months_str[month][0:10]
                months.append("{0}-{1}".format(month_str, str(year)[-4:]))
                next_month = month + 1 if month != 12 else 1
                next_year = year + 1 if next_month == 1 else year
                date1 = date1.replace(month=next_month, year=next_year)
            AdminuserModel.objects.create(
                subadmin_id=request.POST['subadmin_id'],
                username=request.POST['username'],
                lastname=request.POST['lastname'],
                age=request.POST['age'],
                gender=request.POST['gender'],
                email=request.POST['email'],
                password=request.POST['password'],
                mobile=request.POST['mobile'],
                address=request.POST['address'],
                # goal=request.POST['goal'],
                subscription_from_time=request.POST['subscription_from_time'],
                subscription_to_time=request.POST['subscription_to_time'],
                months=months,
            )
            admin = AdminuserModel.objects.latest("pk")
            for i in request.POST.getlist('income_categories'):
                UserincomeCategory.objects.create(admin=admin,income_category_name=i)
            messages.add_message(request, messages.SUCCESS, 'user added successfully')
            return redirect('adminusers')
    else:
            subadmindata=SubadminauthModel.objects.all()
            income_category = IncomecategoryModel.objects.all()
            data = {'adminusser_page': 'active','subadmindata':subadmindata,'income_category':income_category}
            return render(request, 'admin_template/users/addusers.html', data)

@checkadminauth
def deleteuser(request):
    if request.method=='POST':
        userid=request.POST['userid']
        data=AdminuserModel.objects.get(id=userid)
        data.delete()
        messages.add_message(request, messages.SUCCESS, 'user deleted successfully')
        return redirect('adminusers')

def edituser(request,pk):
    userdata=AdminuserModel.objects.get(pk=pk)
    income_category = UserincomeCategory.objects.filter(admin=userdata.pk)
    income_category_list= []
    for selected_category in income_category:
        income_category_list.append(selected_category.income_category_name)
    income_categories = IncomecategoryModel.objects.all()
    subadmindata = SubadminauthModel.objects.all()
    data = {'adminusser_page': 'active','userdata':userdata,'subadmindata':subadmindata,'income_categories':income_categories,'income_category':income_category_list}
    return render(request, 'admin_template/users/editusers.html', data)

@checkadminauth
def updateusers(request):
    if request.method=='POST':
        subscription_from_time = request.POST['subscription_from_time']
        subscription_to_time = request.POST['subscription_to_time']
        date1 = datetime.strptime(subscription_from_time, "%Y-%m-%d")
        date2 = datetime.strptime(subscription_to_time, "%Y-%m-%d")
        date1 = date1.replace(day=1)
        date2 = date2.replace(day=1)
        months_str = calendar.month_name
        months = []
        while date1 < date2:
            month = date1.month
            year = date1.year
            month_str = months_str[month][0:10]
            months.append("{0}-{1}".format(month_str, str(year)[-4:]))
            next_month = month + 1 if month != 12 else 1
            next_year = year + 1 if next_month == 1 else year
            date1 = date1.replace(month=next_month, year=next_year)

        usersids=request.POST['usersids']

        userdata=AdminuserModel.objects.get(id=usersids)
        userdata.subadmin_id=request.POST['subadmin_id']
        userdata.username=request.POST['username']
        userdata.age=request.POST['age']
        userdata.gender=request.POST['gender']
        userdata.email=request.POST['email']
        userdata.mobile=request.POST['mobile']
        userdata.address=request.POST['address']
        # userdata.goal=request.POST['goal']
        userdata.password=request.POST['password']
        userdata.subscription_from_time=request.POST['subscription_from_time']
        userdata.subscription_to_time=request.POST['subscription_to_time']
        userdata.months=months
        userdata.save()

        income_category = UserincomeCategory.objects.filter(admin=userdata.pk)
        for incm_cat in income_category:
            incm_cat.delete()

        admin = AdminuserModel.objects.get(pk=userdata.pk)
        for income_category in request.POST.getlist('income_categories'):
            userincomecategory = UserincomeCategory()
            userincomecategory.income_category_name = income_category
            userincomecategory.admin = admin
            userincomecategory.save()

        messages.add_message(request, messages.SUCCESS, 'user updated successfully')
        return redirect('adminusers')

def view_estimate_expanse(request,id):
    userdata = AdminuserModel.objects.get(id=id)
    month = userdata.months
    data = month[1:-1]
    data2 = data.split(',')
    totalmonths = []
    for newdata2 in data2:
        data3 = newdata2.replace("'", "")
        totalmonths.append(data3)
    monthdata = []
    for newtotalmonths in totalmonths:
        data4 = {}
        data4['month_name'] = newtotalmonths
        # for income
        incomedata = IncomeModel.objects.filter(user_id=id, month=newtotalmonths).values()
        TotalIncome = 0
        FinalIncome = []
        for newincomedata in incomedata:
            f_income = int(TotalIncome) + int(newincomedata['income'])
            FinalIncome.append(f_income)
        # for tax
        taxdata = TaxModel.objects.filter(user_id=id, month=newtotalmonths).values()
        TotalTax = 0
        FinalTax = []
        for newtaxdata in taxdata:
            f_tax = int(TotalTax) + int(newtaxdata['tax_per'])
            FinalTax.append(f_tax)
        data4['total_tax'] = sum(FinalTax)
        # savings
        savingsdata = SavingsModel.objects.filter(user_id=id, month=newtotalmonths).values()
        TotalSavings = 0
        FinalSavings = []
        for newsavingsdata in savingsdata:
            f_saving = int(TotalSavings) + int(newsavingsdata['saving_per'])
            FinalSavings.append(f_saving)
        data4['total_savings'] = sum(FinalSavings)
        # Expanse
        TotalExpense = 0
        FinalExpense = []
        expensedata = ExpensesModel.objects.filter(user_id=id, month=newtotalmonths).values()
        for newexpensedata in expensedata:
            f_expense = int(TotalExpense) + int(newexpensedata['total_expenses'])
            FinalExpense.append(f_expense)
        data4['total_expanse'] = sum(FinalExpense)
        # calculation of tax amount
        total_adition = (sum(FinalTax) + sum(FinalSavings))
        TaxincludedTotal = ((total_adition) / 100) * (sum(FinalIncome))
        Taxincluded_FinalTotal = sum(FinalIncome) - TaxincludedTotal
        data4['total_income'] = Taxincluded_FinalTotal
        monthdata.append(data4)
    from_date = userdata.subscription_from_time.strftime('%m/%d/%Y')
    to_date = userdata.subscription_to_time.strftime('%m/%d/%Y')
    data = {'monthlyexpenses_page': 'active',
            'userdata': userdata,
            'monthdata': monthdata,
            'from_date': from_date,
            'to_date': to_date,
            }
    return render(request, 'admin_template/users/view_estimate_expanse/view_estimate_expanse.html', data)

def monthwise_estimate(request):
    month=request.POST['month']
    user_id=request.POST['user_id']
    userdata=AdminuserModel.objects.get(id=user_id)
    #income
    incomedata=IncomeModel.objects.filter(user_id=user_id,month=month).values()
    TotalIncome=0
    FinalIncome=[]
    for newincomedata in incomedata:
        f_income=int(TotalIncome)+int(newincomedata['income'])
        FinalIncome.append(f_income)
    #tax
    alltax = TaxcategoryModel.objects.all()
    taxdata = TaxModel.objects.filter(user_id=user_id, month=month).values()
    TotalTax = 0
    FinalTax = []
    for newtaxdata in taxdata:
        taxcategory = TaxcategoryModel.objects.get(id=newtaxdata['tax_category_id'])
        newtaxdata['tax_category_name'] = taxcategory.tax_category_name
        f_tax = int(TotalTax) + int(newtaxdata['tax_per'])
        FinalTax.append(f_tax)
    #savings
    savingsdata = SavingsModel.objects.filter(user_id=user_id, month=month).values()
    TotalSavings = 0
    FinalSavings = []
    for newsavingsdata in savingsdata:
        savingcategory = SavingcategoryModel.objects.get(id=newsavingsdata['saving_category_id'])
        newsavingsdata['saving_category_name'] = savingcategory.saving_category_name
        f_saving = int(TotalSavings) + int(newsavingsdata['saving_per'])
        FinalSavings.append(f_saving)
    savingcategory=SavingcategoryModel.objects.all()
    #expense
    budget_master_category = BudgetcategoriesModel.objects.all()
    TotalExpense = 0
    FinalExpense = []
    expensedata=ExpensesModel.objects.filter(user_id=user_id, month=month).values()
    for newexpensedata in expensedata:
        f_expense = int(TotalExpense) + int(newexpensedata['total_expenses'])
        FinalExpense.append(f_expense)
        mastercategory=BudgetcategoriesModel.objects.get(id=newexpensedata['master_category_id'])
        newexpensedata['master_category_name']=mastercategory.category_name
        category=BudgetsubcategoriesModel.objects.get(id=newexpensedata['category_id'])
        newexpensedata['category_name']=category.subcategory_name
        subcategory = BudgetlastcategoriesModel.objects.get(id=newexpensedata['subcategory_id'])
        newexpensedata['subcategory_name'] = subcategory.last_category_name
    #calculation of tax amount
    percentage = (sum(FinalTax) + sum(FinalSavings))
    taxamount = ((percentage) / 100) * (sum(FinalIncome))
    Taxincluded_FinalTotal = sum(FinalIncome) - taxamount
    data={'monthlyexpenses_page':'active',
          'month_name':month,
          'incomedata':incomedata, #income
          'FinalIncome': sum(FinalIncome),  # income total
          'alltax':alltax,
          'taxdata':taxdata, #tax
          'FinalTax':sum(FinalTax), #total tax
          'savingcategory': savingcategory,
          'savingsdata':savingsdata, #saving
          'FinalSavings':sum(FinalSavings), #total saving
          'budget_master_category':budget_master_category,
          'expensedata':expensedata,#expense
          'userdata':userdata,
          'FinalExpense':sum(FinalExpense),
          'Taxincluded_FinalTotal':Taxincluded_FinalTotal
          }
    return render(request, 'admin_template/users/view_estimate_expanse/monthwise_estimate.html', data)



#subadmin functions
@checkadminauth
def subadmin(request):
    subadmindata=SubadminauthModel.objects.all()
    data = {'adminusser_page': 'active','subadmindata':subadmindata}
    return render(request, 'admin_template/users/subadminlist.html', data)

@checkadminauth
def addsubadmin(request):
    if request.method=='POST':
        if 'subadmin_photo' in request.FILES and request.FILES['subadmin_photo']:
            SubadminauthModel.objects.create(
                admin_id=request.session['admin_id'],
                subadmin_name=request.POST['subadmin_name'],
                last_name=request.POST['subadmin_last_name'],
                subadmin_email=request.POST['subadmin_email'],
                subadmin_password=request.POST['subadmin_password'],
                profile_pic=request.FILES['subadmin_photo']
            )
        else:
            SubadminauthModel.objects.create(
                admin_id=request.session['admin_id'],
                subadmin_name=request.POST['subadmin_name'],
                last_name=request.POST['subadmin_last_name'],
                subadmin_email=request.POST['subadmin_email'],
                subadmin_password=request.POST['subadmin_password']
            )
        messages.add_message(request, messages.SUCCESS, 'subadmin inserted successfully')
        return redirect('subadmin')
    else:
        data = {'adminusser_page': 'active'}
        return render(request, 'admin_template/users/addsubadmin.html', data)

@checkadminauth
def deletesubadmin(request):
    if request.method=='POST':
        subadminid=request.POST['subadminid']
        data=SubadminauthModel.objects.get(id=subadminid)
        data.delete()
        messages.add_message(request, messages.SUCCESS, 'subadmin deleted successfully')
        return redirect('subadmin')

@checkadminauth
def editsubadmin(request):
    if request.method=='POST':
        subadminids=request.POST['subadminids']
        subadmindata=SubadminauthModel.objects.get(id=subadminids)
        data = {'adminusser_page': 'active','subadmindata':subadmindata}
        return render(request, 'admin_template/users/editsubadmin.html', data)

@checkadminauth
def updatesubadmin(request):
    if request.method=='POST':
        subadminids=request.POST['subadminids']
        data=SubadminauthModel.objects.get(id=subadminids)
        if 'subadmin_photo' in request.FILES and request.FILES['subadmin_photo']:
            data.subadmin_name=request.POST['subadmin_name'] 
            data.last_name=request.POST['subadmin_last_name'] 
            data.subadmin_email=request.POST['subadmin_email']
            data.subadmin_password=request.POST['subadmin_password']
            data.profile_pic=request.FILES['subadmin_photo']
        else:
            data.subadmin_name=request.POST['subadmin_name']
            data.last_name=request.POST['subadmin_last_name']
            data.subadmin_email=request.POST['subadmin_email']
            data.subadmin_password=request.POST['subadmin_password']
        data.save()
        messages.add_message(request, messages.SUCCESS, 'subadmin updated successfully')
        return redirect('subadmin')

def changeStatus(request):
    if request.method =="POST":
        user = AdminuserModel.objects.filter(id=request.POST['pk'])
        user = AdminuserModel.objects.get(id=user[0].id)
        if user.status:
            user.status = False
        else:
            user.status = True
        user.save()
    return HttpResponse(1)

def changeSubStatus(request):
    if request.method =="POST":
        user = SubadminauthModel.objects.filter(id=request.POST['pk'])
        user = SubadminauthModel.objects.get(id=user[0].id)
        if user.status:
            user.status = False
        else:
            user.status = True
        user.save()
    return HttpResponse(1)

def editaccount(request):
    if request.method=="POST":
        bank_account = UserbankdetailModel.objects.get(pk=request.POST['id'])
        data = "<form method='POST' action='{% ul'updateaccount' %}'><input type='hidden' value='"+ str(bank_account.pk) +"'><br><label>XXXXXXXXXX"+ str(bank_account.account_number) +"</label><br><input type='text' class='form-control' id='bank_amount' value='"+ str(bank_account.current_balance) +"'></form>"
        return HttpResponse(data)
