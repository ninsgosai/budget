from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib import messages
import os
import random
import string
from authentication.middlewares import checkuserauthfunction
from adminusers.models import AdminuserModel
from monthlyexpenses.models import IncomeModel,TaxModel,SavingsModel,ExpensesModel
from admintaxcategory.models import TaxcategoryModel,Goal
from adminsavingcategory.models import SavingcategoryModel
from adminbudgetcategories.models import BudgetcategoriesModel,BudgetsubcategoriesModel,BudgetlastcategoriesModel
from adminusers.models import AdminuserModel,UserbankdetailModel,UsercreditcardModel,UserotherloanModel,UserFamilyModel,UserincomeCategory
from adminsavingcategory.models import IncomecategoryModel
@checkuserauthfunction
def monthlyexpenses(request):
    userdata=AdminuserModel.objects.get(id=request.session['user_id'])
    month=userdata.months
    data = month[1:-1]
    data2 = data.split(',')
    totalmonths=[]
    for newdata2 in data2:
        data3 = newdata2.replace("'", "")
        totalmonths.append(data3)
    monthdata=[]
    for newtotalmonths in totalmonths:
        data4={}
        data4['month_name']=newtotalmonths
        #for income
        incomedata = IncomeModel.objects.filter(user_id=request.session['user_id'], month=newtotalmonths).values()
        TotalIncome = 0
        FinalIncome = []
        for newincomedata in incomedata:
            f_income = int(TotalIncome) + int(newincomedata['income'])
            FinalIncome.append(f_income)
        #for tax
        taxdata = TaxModel.objects.filter(user_id=request.session['user_id'], month=newtotalmonths).values()
        TotalTax = 0
        FinalTax = []
        for newtaxdata in taxdata:
            f_tax = int(TotalTax) + int(newtaxdata['tax_per'])
            FinalTax.append(f_tax)
        data4['total_tax'] = sum(FinalTax)
        # savings
        savingsdata = SavingsModel.objects.filter(user_id=request.session['user_id'], month=newtotalmonths).values()
        TotalSavings = 0
        FinalSavings = []
        for newsavingsdata in savingsdata:
            f_saving = int(TotalSavings) + int(newsavingsdata['saving_per'])
            FinalSavings.append(f_saving)
        data4['total_savings'] = sum(FinalSavings)
        #Expanse
        TotalExpense = 0
        FinalExpense = []
        expensedata = ExpensesModel.objects.filter(user_id=request.session['user_id'], month=newtotalmonths).values()
        for newexpensedata in expensedata:
            f_expense = int(TotalExpense) + int(newexpensedata['total_expenses'])
            FinalExpense.append(f_expense)
        data4['total_expanse'] = sum(FinalExpense)

        #include tax and savings on income
        total_per = (sum(FinalTax) + sum(FinalSavings))
        TaxincludedTotal = ((total_per) / 100) * (sum(FinalIncome))
        Taxincluded_FinalTotal = sum(FinalIncome) - TaxincludedTotal
        data4['total_income'] = Taxincluded_FinalTotal

        monthdata.append(data4)
    from_date = userdata.subscription_from_time.strftime('%m/%d/%Y')
    to_date = userdata.subscription_to_time.strftime('%m/%d/%Y')

    data={'monthlyexpenses_page':'active',
          'userdata':userdata,
          'monthdata':monthdata,
          'from_date':from_date,
          'to_date':to_date
          }
    return render(request,'user_template/monthlyexpenses/monthlyexpenses.html',data)

#Comman Function For All
def add_monthlyexpenses(request,month):

    #goals
    goals = Goal.objects.filter(admin=request.session['user_id'],month=month).values()
    #income
    incomedata=IncomeModel.objects.filter(user_id=request.session['user_id'],month=month).values()
    income_categories = UserincomeCategory.objects.filter(admin=request.session['user_id'])
    TotalIncome=0
    FinalIncome=[]
    for newincomedata in incomedata:
        f_income=int(TotalIncome)+int(newincomedata['income'])
        FinalIncome.append(f_income)
    #tax
    alltax = TaxcategoryModel.objects.all()
    taxdata = TaxModel.objects.filter(user_id=request.session['user_id'], month=month).values()
    TotalTax = 0
    FinalTax = []
    for newtaxdata in taxdata:
        taxcategory = TaxcategoryModel.objects.get(id=newtaxdata['tax_category_id'])
        newtaxdata['tax_category_name'] = taxcategory.tax_category_name
        f_tax = int(TotalTax) + int(newtaxdata['tax_per'])
        FinalTax.append(f_tax)
    #savings
    savingsdata = SavingsModel.objects.filter(user_id=request.session['user_id'], month=month).values()
    TotalSavings = 0
    FinalSavings = []
    for newsavingsdata in savingsdata:
        savingcategory = SavingcategoryModel.objects.get(id=newsavingsdata['saving_category_id'])
        newsavingsdata['saving_category_name'] = savingcategory.saving_category_name
        if not newsavingsdata['saving_per'] or newsavingsdata['saving_per']=="" or newsavingsdata['saving_per']==0:
            newsavingsdata['saving_per'] = 0
        f_saving = int(TotalSavings) + int(newsavingsdata['saving_per'])
        FinalSavings.append(f_saving)
    savingcategory=SavingcategoryModel.objects.all()
    #expense
    budget_master_category = BudgetcategoriesModel.objects.all()
    TotalExpense = 0
    FinalExpense = []
    expensedata=ExpensesModel.objects.filter(user_id=request.session['user_id'], month=month).values()
    for newexpensedata in expensedata:
        if newexpensedata['total_expenses']:
            f_expense = int(TotalExpense) + int(newexpensedata['total_expenses'])
            FinalExpense.append(f_expense)
            mastercategory=BudgetcategoriesModel.objects.get(id=newexpensedata['master_category_id'])
            newexpensedata['master_category_name']=mastercategory.category_name
            category=BudgetsubcategoriesModel.objects.get(id=newexpensedata['category_id'])
            newexpensedata['category_name']=category.subcategory_name
            subcategory = BudgetlastcategoriesModel.objects.get(id=newexpensedata['subcategory_id'])
            newexpensedata['subcategory_name'] = subcategory.last_category_name
    # for applying tax and savings per on income
    total_per = (sum(FinalTax) + sum(FinalSavings))
    TaxincludedTotal = ((total_per) / 100) * (sum(FinalIncome))
    Taxincluded_FinalTotal = sum(FinalIncome) - TaxincludedTotal
    
    data={'monthlyexpenses_page':'active',
          'month_name':month.replace(" ",""),
          'incomedata':incomedata,
          'FinalIncome': sum(FinalIncome),
          'alltax':alltax,
          'taxdata':taxdata,
          'income_categories':income_categories,
          'FinalTax':sum(FinalTax),
          'savingcategory': savingcategory,
          'savingsdata':savingsdata,
          'FinalSavings':sum(FinalSavings),
          'budget_master_category':budget_master_category,
          'expensedata':expensedata,
          'FinalExpense':sum(FinalExpense),
          'goals':goals,
          'Taxincluded_FinalTotal':Taxincluded_FinalTotal,  #tax included final income
          'user': AdminuserModel.objects.get(pk=int(request.session['user_id']))
          }
    return render(request,'user_template/monthlyexpenses/add_monthlyexpenses.html',data)

#Income Functions
def insertusserincome(request):
    if request.method=='POST' :
        IncomeModel.objects.create(
            user_id = request.session['user_id'],
            month = request.POST['month_names'],
            name = request.POST['name'],
            income_category = request.POST['income_category'],
            income = request.POST['income'],
        )
        messages.add_message(request, messages.SUCCESS, 'income data inserted')
        return redirect('add_monthlyexpenses',request.POST['month_names'])

def deleteincome(request):
    if request.method=='POST':
        income_id=request.POST['income_id']
        month=request.POST['month']
        data=IncomeModel.objects.get(id=income_id)
        data.delete()
        messages.add_message(request, messages.SUCCESS, 'income data deleted')
        return redirect('add_monthlyexpenses',month)

def editincome(request):
    if request.method=='POST':
        edit_income_id=request.POST['edit_income_id']
        incomedata=IncomeModel.objects.get(id=edit_income_id)

        incomecategories = UserincomeCategory.objects.filter(admin=request.session['user_id'])
    
        family = UserFamilyModel.objects.filter(adminusermodel=request.session['user_id'])

        strmember ="<option value="+request.session['username']+">"+request.session['username'] + "</option>"
        for member in family:
            if incomedata.name==member.username:
                sel = "selected"
            else:
                sel = ""
            strmember += "<option value="+member.username+" "+sel+">"+member.username + "</option>"

        income_categories = ""
        for member in incomecategories:
            income_categories += "<option value="+member.income_category_name+" >"+member.income_category_name + "</option>"

        data="<form><input type='hidden' name='hidden_month_name' id='hidden_month_name' value='"+incomedata.month+"'><input type='hidden' name='hidden_income_id' id='hidden_income_id' value='"+edit_income_id+"'><div class='form-group'><label>Name</label><select class='form-control' id='edit_name' name='name'>"+strmember+"</select></div><div class='form-group'><label>Income</label><input type='text' value="+incomedata.income+" name='income' class='form-control' id='edit_income_field' placeholder='Income' > <label>Income Category</label><select  class='form-control' name='income_category_in' id='income_category_in' required><option value=''>Select Income Category</option>"+income_categories+"</select></form>"

        # data='<form><input type="hidden" name="hidden_month_name" id="hidden_month_name" value="'+incomedata.month+'"><input type="hidden" name="hidden_income_id" id="hidden_income_id" value="'+edit_income_id+'"><div class="form-group"><label>Name</label><input type="text" class="form-control" id="edit_name"  value="'+incomedata.name+'" name="name" placeholder="Family Member Name"></div><div class="form-group"><label>Income</label><input type="text" value="'+incomedata.income+'" name="income" class="form-control" id="edit_income_field" placeholder="Income" ></div></form>'
        return HttpResponse(data)

def updateincome(request):
    if request.method=='POST':
        hidden_income_id=request.POST['hidden_income_id']
        hidden_month_name=request.POST['hidden_month_name']
        data=IncomeModel.objects.get(id=hidden_income_id)
        data.income=request.POST['income']
        data.name=request.POST['name']
        data.income_category=request.POST['income_category_in']
        data.save()
        return HttpResponse('1')

#Tax Functions
def inserttax(request):
    if request.method=='POST':
        month_names=request.POST['month_names']
        TaxModel.objects.create(
            user_id=request.session['user_id'],
            tax_category_id=request.POST['tax_category_id'],
            member_name=request.POST['member_name'],
            tax_per=request.POST['tax_per'],
            tax_amt=request.POST['tax_amt'],
            month=month_names
        )
        messages.add_message(request, messages.SUCCESS, 'tax data inserted')
        return redirect('add_monthlyexpenses',month_names)

def deletetax(request):
    if request.method=='POST':
        month=request.POST['month']
        tax_id=request.POST['tax_id']
        datas=TaxModel.objects.get(id=tax_id)
        datas.delete()
        messages.add_message(request, messages.SUCCESS, 'tax data deleted')
        return redirect('add_monthlyexpenses', month)

def edittax(request):
    if request.method=='POST':
        tax_id=request.POST['tax_id']
        usertaxdata=TaxModel.objects.get(id=tax_id)
        taxcategory=TaxcategoryModel.objects.all()

        family = UserFamilyModel.objects.filter(adminusermodel=request.session['user_id'])
        strmember ="<option value="+request.session['username']+">"+request.session['username'] + "</option>"
        for member in family:
            if usertaxdata.member_name==member.username:
                sel = "selected"
            else:
                sel = ""
            strmember += "<option value="+member.username+" "+sel+">"+member.username + "</option>"

        data='<form><input type="hidden" id="edit_tax_id" value="'+tax_id+'"><input type="hidden" id="edit_month_name" value="'+usertaxdata.month+'"><div class="form-group"><label>Tax Category</label><select class="form-control mb-2 mr-sm-2" id="edit_tax_category" name="edit_tax_category"><option selected>--select tax category</option>'
        data2=[]
        for newtaxcategory in taxcategory:
            if (newtaxcategory.id == usertaxdata.tax_category_id):
                fetched_value='selected'
            else:
                fetched_value=''
            option='<option value="'+str(newtaxcategory.id)+'" '+fetched_value+'>'+newtaxcategory.tax_category_name+'</option>'
            data2.append(option)
        data3="</select></div><div class='form-group'><label>Family Member Name</label><select class='form-control' id='edit_member_name' name='edit_member_name'>"+strmember+"</select></div><div class='form-group'><label>Tax (%)</label><input type='text' name='edit_tax_per' class='form-control' oninput='editcalculateAmount()' id='edit_tax_per' value="+usertaxdata.tax_per+" placeholder='Tax(%)'><label>Tax (Amount)</label><input type='text' name='edit_tax_amt' class='form-control' id='edit_tax_amt' oninput='editcalculatePercentage()' value='"+usertaxdata.tax_amt+"' placeholder='Tax(Amount)'></div><div class='modal-footer'><button type='button' class='btn btn-danger btn-pill' data-dismiss='modal'>Close</button><button type='button' id='update_tax' class='btn btn-primary btn-pill'>Update</button></div></form>"

        # data3='</select></div><div class="form-group"><label>Family Member Name</label><input type="text" class="form-control" id="edit_member_name"  name="edit_member_name" placeholder="Family Member Name" value="'+usertaxdata.member_name+'"></div><div class="form-group"><label>Income</label><input type="text" name="edit_tax_per" class="form-control" id="edit_tax_per" value="'+usertaxdata.tax_per+'" placeholder="Tax(%)" ></div></form>'
        finaldata=data+str(data2)+data3
        return HttpResponse(finaldata)

def updatetax(request):
    if request.method=='POST':
        edit_month_name=request.POST['edit_month_name']
        data=TaxModel.objects.get(id=request.POST['edit_tax_id'])
        data.tax_category_id=request.POST['edit_tax_category']
        data.member_name=request.POST['edit_member_name']
        data.tax_per=request.POST['edit_tax_per']
        data.tax_amt=request.POST['edit_tax_amt']
        data.save()
        return HttpResponse('1')

#Savings Functions
def insertsavings(request):
    if request.method=='POST':
        month_names=request.POST['month_names']
        SavingsModel.objects.create(
            user_id=request.session['user_id'],
            saving_category_id=request.POST['saving_category_id'],
            family_member_name=request.POST['family_member_name'],
            saving_per=request.POST['saving_per'],
            saving_amt=request.POST['saving_amt'],
            month=month_names
        )
        messages.add_message(request, messages.SUCCESS, 'savings data inserted')
        return redirect('add_monthlyexpenses', month_names)

def deletesavings(request):
    if request.method == 'POST':
        month = request.POST['month']
        saving_id = request.POST['saving_id']
        savingdata = SavingsModel.objects.get(id=saving_id)
        savingdata.delete()
        messages.add_message(request, messages.SUCCESS, 'savings data deleted')
        return redirect('add_monthlyexpenses', month)

def editsavings(request):
    if request.method=='POST':
        saving_id=request.POST['saving_id']
        usersavingsdata=SavingsModel.objects.get(id=saving_id)
        savingcategory=SavingcategoryModel.objects.all()

        family = UserFamilyModel.objects.filter(adminusermodel=request.session['user_id'])
        strmember ="<option value="+request.session['username']+">"+request.session['username'] + "</option>"
        for member in family:
            if usersavingsdata.family_member_name==member.username:
                sel = "selected"
            else:
                sel = ""
            strmember += "<option value="+member.username+" "+sel+">"+member.username + "</option>"

        data='<form><input type="hidden" id="edit_savings_id" value="'+saving_id+'"><input type="hidden" id="edit_month_name" value="'+usersavingsdata.month+'"><div class="form-group"><label>Savings Category</label><select class="form-control mb-2 mr-sm-2" id="edit_saving_category" name="edit_saving_category"><option selected>--select saving category</option>'
        data2=[]
        for newsavingcategory in savingcategory:
            if newsavingcategory.id == usersavingsdata.saving_category_id:
                optionval='selected'
            else:
                optionval=''
            option='<option value="'+str(newsavingcategory.id)+'"'+optionval+'>'+newsavingcategory.saving_category_name+'</option>'
            data2.append(option)

        data3="</select></div><div class='form-group'><label>Family Member Name</label><select class='form-control' id='edit_family_member_name' name='edit_family_member_name'>"+strmember+"</select></div><div class='form-group'><label>Saving per(%)</label><input type='text' name='edit_savings_per' class='form-control' id='edit_savings_per' oninput='savingeditcalculateAmount()' value='"+usersavingsdata.saving_per+"' placeholder='Tax(%)' > <label>Saving amount($)</label><input type='text' oninput='savingeditcalculatePercentage()' name='edit_savings_amt' class='form-control' id='edit_savings_amt' value='"+usersavingsdata.saving_amt+"' placeholder='Tax(Amount)' ></div></div><div class='modal-footer'><button type='button' class='btn btn-danger btn-pill' data-dismiss='modal'>Close</button><button type='button' id='update_savings' class='btn btn-primary btn-pill'>Update</button></div></form>"

        # data3='</select></div><div class="form-group"><label>Family Member Name</label><input type="text" class="form-control" id="edit_family_member_name"  name="edit_family_member_name" placeholder="Family Member Name" value="'+usersavingsdata.family_member_name+'"></div><div class="form-group"><label>Saving per(%)</label><input type="text" name="edit_savings_per" class="form-control" id="edit_savings_per" value="'+usersavingsdata.saving_per+'" placeholder="Tax(%)" ></div></form>'

        finaldata=data+str(data2)+data3
        return HttpResponse(finaldata)

def updatesavings(request):
    if request.method=='POST':
        edit_month_name=request.POST['edit_month_name']
        data=SavingsModel.objects.get(id=request.POST['edit_savings_id'])
        data.saving_category_id=request.POST['edit_saving_category']
        data.family_member_name=request.POST['edit_family_member_name']
        data.saving_per=request.POST['edit_savings_per']
        data.saving_amt=request.POST['edit_savings_amt']
        data.save()
        return HttpResponse('1')

#Expenses Functions
def getcategory(request):
    if request.method=='POST':
        master_category_id=request.POST['master_category_id']
        category=BudgetsubcategoriesModel.objects.filter(budget_category_id=master_category_id)
        one='<select onchange="CategoryFunction()" class="form-control mb-2 mr-sm-2" required id="category_id" name="category_id"><option>--select category--</option>'
        data=[]
        for newcategory in category:
            two='<option value='+str(newcategory.id)+'>'+newcategory.subcategory_name+'</option>'
            data.append(two)
        three='</select>'
        finaldata=one+str(data)+three
        return HttpResponse(finaldata)

def getsubcategory(request):
    if request.method=='POST':
        category_id=request.POST['category_id']
        subcategory=BudgetlastcategoriesModel.objects.filter(budget_subcategory_id=category_id)
        one='<select  class="form-control mb-2 mr-sm-2" id="subcategory_id" required name="subcategory_id"><option value="">--select sub category--</option>'
        data=[]
        for newsubcategory in subcategory:
            two='<option value='+str(newsubcategory.id)+'>'+newsubcategory.last_category_name+'</option>'
            data.append(two)
        three='</select>'
        finaldata=one+str(data)+three
        return HttpResponse(finaldata)

month_number = {
    'January': 1,
    'February':2,
    'March':3,
    'April':4,
    'May':5,
    'June':6,
    'July':7,
    'August':8,
    'September':9,
    'October':10,
    'November':11,
    'December':12,
}
def insertexpenses(request):
    if request.method=='POST':
        current_month = month_number[request.POST['month_names'][:-5]]
        current_year = request.POST['month_names'][-5:]
        months = request.POST.getlist("tets")
        if 'syncing_fund' in request.POST and request.POST['syncing_fund'] == "on":
            for month in months:
                if current_month <= month_number[month]:
                    ExpensesModel.objects.create(
                        master_category_id=request.POST['master_category_id'],
                        category_id=request.POST['category_id'],
                        subcategory_id=request.POST['subcategory_id'],
                        total_expenses=float(int(request.POST['total_expenses']) / int(request.POST['syncing_month'])),
                        syncing_amount=request.POST['total_expenses'],
                        syncing_month=request.POST['syncing_month'],
                        month=str(month).replace(" ","") + str(current_year),
                        user_id=request.session['user_id'],
                    )
                else:
                    ExpensesModel.objects.create(
                        master_category_id=request.POST['master_category_id'],
                        category_id=request.POST['category_id'],
                        subcategory_id=request.POST['subcategory_id'],
                        total_expenses=float(int(request.POST['total_expenses']) / int(request.POST['syncing_month'])),
                        syncing_amount=request.POST['total_expenses'],
                        syncing_month=request.POST['syncing_month'],
                        month= str(month).replace(" ","") +str(int(current_year) + 1),
                        user_id=request.session['user_id'],
                    )
        else:
            ExpensesModel.objects.create(
                master_category_id=request.POST['master_category_id'],
                category_id=request.POST['category_id'],
                subcategory_id=request.POST['subcategory_id'],
                total_expenses=int(request.POST['total_expenses']),
                syncing_amount=request.POST['total_expenses'],
                syncing_month=request.POST['syncing_month'],
                month=request.POST['month_names'],
                user_id=request.session['user_id'],
            )
        messages.add_message(request, messages.SUCCESS, 'expense data inserted')
        return redirect('add_monthlyexpenses', request.POST['month_names'])

def deleteexpenses(request):
     if request.method=='POST':
         month=request.POST['month']
         expense_id=request.POST['expense_id']
         exdata=ExpensesModel.objects.get(id=expense_id)
         exdata.delete()
         messages.add_message(request, messages.SUCCESS, 'expense data deleted')
         return redirect('add_monthlyexpenses',month)

def editexpense(request):
    if request.method=='POST':
        expense_id=request.POST['expense_id']
        userexpensedata=ExpensesModel.objects.get(id=expense_id)
        mastercategory=BudgetcategoriesModel.objects.all()
        category=BudgetsubcategoriesModel.objects.all()
        subcategory=BudgetlastcategoriesModel.objects.all()
        data1 = '<form><input type="hidden" id="edit_expenses_id" value="' + expense_id + '"><input type="hidden" id="edit_month_name" value="' + userexpensedata.month + '"><div class="form-group"><label>Master Category</label><select class="form-control mb-2 mr-sm-2" id="edit_master_category_id" name="edit_master_category_id"><option selected>--select master category</option>'
        data2 = []
        for newmastercategory in mastercategory:
            if newmastercategory.id==userexpensedata.master_category_id:
                valueone='selected'
            else:
                valueone=''
            option = '<option value="'+str(newmastercategory.id)+'" '+valueone+'>'+newmastercategory.category_name+'</option>'
            data2.append(option)
        data3 = '</select>'

        data4='<div class="form-group"><label>Category</label><select  class="form-control mb-2 mr-sm-2" id="edit_category" name="edit_category"><option selected>--select category--</option>'
        data5 = []
        for newcategory in category:
            if newcategory.id==userexpensedata.category_id:
                valuetwo='selected'
            else:
                valuetwo=''
            option2 = '<option value="'+str(newcategory.id)+'" '+valuetwo+'>'+newcategory.subcategory_name+'</option>'
            data5.append(option2)
        data6 = '</select>'

        data7 = '<div class="form-group"><label>Subcategory</label><select class="form-control mb-2 mr-sm-2" id="edit_subcategory" name="edit_subcategory"><option selected>--select subcategory--</option>'
        data8 = []
        for newsubcategory in subcategory:
            if newsubcategory.id==userexpensedata.subcategory_id:
                valuethree='selected'
            else:
                valuethree=''
            option2 = '<option value="' + str(newsubcategory.id) + '" '+valuethree+'>' + newsubcategory.last_category_name + '</option>'
            data8.append(option2)
        data9 = '</select>'
        data10=' </div><div class="form-group"><label>Expense</label><input type="text" class="form-control mb-2 mr-sm-2" placeholder="Total Expenses (Amount Only)" name="edit_total_expenses" id="edit_total_expenses" value="'+str(userexpensedata.total_expenses)+'" ></div></form>'
        finaldata = data1 + str(data2) + data3 + data4 + str(data5) + data6 + data7 + str(data8) + data9 + data10
        return HttpResponse(finaldata)

def updateexpensedata(request):
    if request.method=='POST':
        edit_expenses_id=request.POST['edit_expenses_id']
        data = ExpensesModel.objects.get(id=edit_expenses_id)
        data.master_category_id=request.POST['edit_master_category_id']
        data.category_id=request.POST['edit_category']
        data.subcategory_id=request.POST['edit_subcategory']
        data.total_expenses=request.POST['edit_total_expenses']
        data.save()
        return HttpResponse('1')

#=====================third=============================================================================================

#comman for all
def userestimates(request):
    userdata = AdminuserModel.objects.get(id=request.session['user_id'])
    month = userdata.months
    data = month[1:-1]
    data2 = data.split(',')
    expense_category = ExpensesModel.objects.filter(user=userdata)

    expense_list = []
    
    totalmonths = []
    for newdata2 in data2:
        data3 = newdata2.replace("'", "")
        data3 = data3.replace(" ", "")
        totalmonths.append(data3)

    monthdata = []
    for newtotalmonths in totalmonths:
        data4 = {}
        data4['month_name'] = newtotalmonths
        #income
        admin = AdminuserModel.objects.get(pk=request.session['user_id'])
        incomedata = IncomeModel.objects.filter(user=admin, month=newtotalmonths).values()
        TotalIncome = 0
        FinalIncome = []

        for newincomedata in incomedata:
            f_income = int(TotalIncome) + int(newincomedata['income'])
            FinalIncome.append(f_income)
        data4['total_income'] = sum(FinalIncome)
        # tax
        taxdata = TaxModel.objects.filter(user_id=request.session['user_id'], month=newtotalmonths).values()
        TotalTax = 0
        FinalTax = []
        for newtaxdata in taxdata:
            f_tax = int(TotalTax) + int(newtaxdata['tax_per'])
            FinalTax.append(f_tax)
            actual_category = BudgetlastcategoriesModel.objects.get(pk =newtaxdata['id'])
            if actual_category not in expense_list:
                expense_list.append(actual_category.last_category_name)
        data4['total_tax'] = sum(FinalTax)
        monthdata.append(data4)

       
    #for income
    uniqdata = IncomeModel.objects.filter(user_id=request.session['user_id']).values('is_row').distinct()
    allincome = []
    for newuniqdata in uniqdata:
        incomeobject = {}
        incomedata = IncomeModel.objects.filter(is_row=newuniqdata['is_row'])
        for newincomedata in incomedata:
            incomeobject.update({'name': newincomedata.name})
            incomeobject.update({'is_row': newincomedata.is_row})
        incomeobject.update({'incomedata': incomedata})
        allincome.append(incomeobject)
    #for tax
    tax_category=TaxcategoryModel.objects.all()
    taxdata = TaxModel.objects.filter(user_id=request.session['user_id']).values('tax_row').distinct()
    alltax = []
    for newtaxdata in taxdata:
        taxobject = {}
        tax = TaxModel.objects.filter(tax_row=newtaxdata['tax_row'])
        for newtax in tax:
            taxobject.update({'member_name': newtax.member_name})
            taxobject.update({'tax_row': newtax.tax_row})
        taxobject.update({'tax': tax})
        alltax.append(taxobject)
    # for savings
    savings_category = SavingcategoryModel.objects.all()
    savingsdata = SavingsModel.objects.filter(user_id=request.session['user_id']).values('saving_row').distinct()
    allsavings = []
    for newsavingsdata in savingsdata:
        savingsobject = {}
        saving = SavingsModel.objects.filter(saving_row=newsavingsdata['saving_row'])
        for newsaving in saving:
            savingsobject.update({'family_member_name': newsaving.family_member_name})
            savingsobject.update({'saving_row': newsaving.saving_row})
        savingsobject.update({'saving': saving})
        allsavings.append(savingsobject)
    if monthdata[0]['month_name']=='':
        err = False
    else:
        err = True
    data = {'monthlyexpenses_page': 'active',
            'totalmonths':totalmonths,
            'allincome':allincome, #income
            'tax_category':tax_category, #tax
            'alltax':alltax, #tax
            'savings_category':savings_category, #savings
            'allsavings':allsavings, #savings
            'monthdata':monthdata, #savings
            'err':err,
            'expense_list':expense_list # Expense Category
            }
    return render(request, 'user_template/monthlyexpenses/monthlyexpenses.html', data)

##for income
def savename(request):
    if request.method=='POST':
        name=request.POST['name']
        userdata = AdminuserModel.objects.get(id=request.session['user_id'])
        month = userdata.months
        data = month[1:-1]
        data2 = data.split(',')
        totalmonths = []
        for newdata2 in data2:
            data3 = newdata2.replace("'", "")
            totalmonths.append(data3)

        letters = string.ascii_lowercase
        is_row=(''.join(random.choice(letters) for i in range(10)))
        for newtotalmonths in totalmonths:
            IncomeModel.objects.create(
                user_id=request.session['user_id'],
                month=newtotalmonths,
                name=name,
                income=0,
                is_row=is_row
            )
        return HttpResponse(1)

def insertincome(request):
    if request.method=='POST':
        income_id=request.POST['income_id']
        income=request.POST['income']
        data=IncomeModel.objects.get(id=income_id)
        data.income=income
        data.save()
        return HttpResponse('1')

def updatename(request):
    if request.method=='POST':
        name=request.POST['name']
        IncomeModel.objects.filter(is_row=request.POST['is_row']).update(name=name)
        return HttpResponse('1')

##for tax
def inserttaxname(request):
    if request.method=='POST':
        family_member_name_tax=request.POST['family_member_name_tax']
        userdata = AdminuserModel.objects.get(id=request.session['user_id'])
        month = userdata.months
        data = month[1:-1]
        data2 = data.split(',')
        totalmonths = []
        for newdata2 in data2:
            data3 = newdata2.replace("'", "")
            totalmonths.append(data3)

        letters = string.ascii_lowercase
        tax_row = (''.join(random.choice(letters) for i in range(10)))
        for newtotalmonths in totalmonths:
            TaxModel.objects.create(
                user_id=request.session['user_id'],
                month=newtotalmonths,
                member_name=family_member_name_tax,
                tax_per=0,
                tax_row=tax_row
            )
        return HttpResponse('1')

def updatetaxcategory(request):
    if request.method=='POST':
        tax_category_id=request.POST['tax_category_id']
        tax_id=request.POST['tax_id']
        data=TaxModel.objects.get(id=tax_id)
        data.tax_category_id=tax_category_id
        data.save()
        return HttpResponse('1')

def edittaxper(request):
    if request.method=='POST':
        tax_per=request.POST['tax_per']
        tax_id=request.POST['tax_id']
        data=TaxModel.objects.get(id=tax_id)
        data.tax_per=tax_per
        data.save()
        return HttpResponse('1')

def updatemembername(request):
    if request.method=='POST':
        member_name=request.POST['member_name']
        tax_row=request.POST['tax_row']
        TaxModel.objects.filter(tax_row=tax_row).update(member_name=member_name)
        return HttpResponse('1')


#for savings
def savesavingsname(request):
    if request.method=='POST':
        family_member_name=request.POST['family_member_name']
        userdata = AdminuserModel.objects.get(id=request.session['user_id'])
        month = userdata.months
        data = month[1:-1]
        data2 = data.split(',')
        totalmonths = []
        for newdata2 in data2:
            data3 = newdata2.replace("'", "")
            totalmonths.append(data3)

        letters = string.ascii_lowercase
        saving_row = (''.join(random.choice(letters) for i in range(10)))
        for newtotalmonths in totalmonths:
            SavingsModel.objects.create(
                user_id=request.session['user_id'],
                month=newtotalmonths,
                family_member_name=family_member_name,
                saving_per=0,
                saving_row=saving_row
            )
        return HttpResponse('1')

def insertsavingsper(request):
    if request.method=='POST':
        saving_category_id=request.POST['saving_category_id']
        saving_id=request.POST['saving_id']
        data=SavingsModel.objects.get(id=saving_id)
        data.saving_category_id=saving_category_id
        data.save()
        return HttpResponse('1')

def updatesavingper(request):
    if request.method=='POST':
        saving_per=request.POST['saving_per']
        saving_id=request.POST['saving_id']
        data=SavingsModel.objects.get(id=saving_id)
        data.saving_per=saving_per
        data.save()
        return HttpResponse('1')

def updatesavingname(request):
    if request.method=='POST':
        saving_row=request.POST['saving_row']
        family_member_names=request.POST['family_member_names']
        SavingsModel.objects.filter(saving_row=saving_row).update(family_member_name=family_member_names)
        return HttpResponse('1')

def editgoal(request):
    if request.method=="POST":
        goal = Goal.objects.get(id=request.POST['id'])
        data = "<form method='POST' action='{% url 'updategoal' %}'><input type='hidden' name='goalid' id='goalid' value='"+ str(goal.pk) +"'><input type='text' name='newgoal' id='newgoal' class='form-control' value='" + str(goal.goal) +"'><br><input type='number' name='goalamount' id='goalamount' class='form-control' value='" + str(goal.goal_amount) + "'><br><input type='date' class='form-control'name='goal_start_date' id='goal_start_date' value='"+ str(goal.start_date)+"'><br><input type='date'class='form-control' name='goal_end_date' id='goal_end_date' value='" + str(goal.deadline_date) + "'><div class='modal-footer'><button type='button' class='btn btn-danger btn-pill' data-dismiss='modal'>Close</button><button type='button' onclick='updateGoal("+str(goal.pk)+")' id='update_goal' class='btn btn-primary btn-pill'>Update</button></div></form>"
        return HttpResponse(data)

def updategoal(request):
    if request.method=="POST":
        goal = Goal.objects.get(id=request.POST['goal'])
        goal.goal=request.POST['newgoal']
        goal.goal_amount=request.POST['goalamount']
        goal.start_date=request.POST['goalstartdate']
        goal.deadline_date=request.POST['goalenddate']
        goal.save()
        
    return HttpResponse('1')

def delete_goal(request):
    if request.method =="POST":
        month = request.POST['month_names']
        goal = Goal.objects.get(pk=request.POST['goal_id'])
        goal.delete()
        messages.add_message(request, messages.SUCCESS, 'goal data Deleted')

    return redirect("add_monthlyexpenses",month)