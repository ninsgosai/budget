from django.shortcuts import render,redirect
from django.template import loader
from django.http import HttpResponse
from django.contrib import messages
import os

from actualexpenses.models import ActualexpenseModel
from adminusers.models import AdminuserModel,SubadminauthModel,UserbankdetailModel,UsercreditcardModel,UserotherloanModel
from adminbudgetcategories.models import BudgetcategoriesModel,BudgetsubcategoriesModel,BudgetlastcategoriesModel

def actualexpenses(request):
    userdata = AdminuserModel.objects.get(id=request.session['user_id'])
    month = userdata.months
    data = month[1:-1]
    data2 = data.split(',')
    totalmonths = []
    for newdata2 in data2:
        data3 = newdata2.replace("'", "")
        data3 = data3.replace(" ", "")
        totalmonths.append(data3)
    monthdata = []

    expense_category = ActualexpenseModel.objects.filter(user_id=userdata.pk)
    
    for newtotalmonths in totalmonths:
        data4 = {}
        data4['month_name'] = newtotalmonths
        expensedata = ActualexpenseModel.objects.filter(user_id=request.session['user_id'], is_month=newtotalmonths).values()
        TotalExpense = 0
        FinalExpense = []
        TotalIncome = 0
        FinalIncome = []
        expense_list = []
        for newexpensedata in expensedata:
            if newexpensedata['actual_expense']:
                f_expense = float(TotalExpense) + float(newexpensedata['actual_expense'])
                FinalExpense.append(f_expense)
                actual_category = BudgetlastcategoriesModel.objects.get(pk =newexpensedata['actual_subcategory_id'])
                if actual_category not in expense_list:
                    expense_list.append(actual_category.last_category_name)
            if newexpensedata['actual_income']:
                f_income = float(TotalIncome) + float(newexpensedata['actual_income'])
                FinalIncome.append(f_income)
        # data4['total_expense'] = sum(FinalExpense) #total expense for perticular month
        data4['total_expense'] = "{:.0f}".format(sum(FinalExpense)) #total expense for perticular month
        data4['total_income'] = "{:.0f}".format(sum(FinalIncome))  #total income for perticular month
        data4['expense_list'] = expense_list
        monthdata.append(data4)
    from_date = userdata.subscription_from_time.strftime('%m/%d/%Y')
    to_date = userdata.subscription_to_time.strftime('%m/%d/%Y')
    data={'actualexpenses_page':'active',
          'userdata':userdata,
          'monthdata':monthdata,
          'from_date':from_date,
          'to_date':to_date,
          'expense_list':expense_list
          }
    return render(request,'user_template/actualexpenses/actualexpenses.html',data)

def add_actualexpenses(request,month):
    bankaccounts=UserbankdetailModel.objects.filter(user_id=request.session['user_id'])
    creditcards=UsercreditcardModel.objects.filter(user_id=request.session['user_id'])
    mastercategory=BudgetcategoriesModel.objects.all()
    data = {'actualexpenses_page': 'active',
            'month':month,
            'mastercategory':mastercategory,
            'creditcards':creditcards,
            'bankaccounts':bankaccounts}
    return render(request, 'user_template/actualexpenses/add_actualexpenses.html', data)

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
def inertexpense(request):
    if request.method=='POST':
         if request.POST['payment_type']=='bank':
            credit_account_number=0
            bank_account_number=request.POST['bank_account_number']
         elif request.POST['payment_type']=='credit':
            bank_account_number=0
            credit_account_number=request.POST['credit_account_number']
         else:
            credit_account_number=0
            bank_account_number=0
         if request.POST['payment_category']=="expense":
            current_month = month_number[request.POST['is_month'][:-5]]
            current_year = request.POST['is_month'][-5:]
            months = request.POST.getlist("tets")
            if 'syncing_fund' in request.POST and request.POST['syncing_fund'] == "on":
                for month in months:
                    if current_month <= month_number[month]:
                        ActualexpenseModel.objects.create(
                            user_id=request.session['user_id'],
                            is_month=str(month).replace(" ","") + str(current_year),
                            payment_category=request.POST['payment_category'],
                            payment_type=request.POST['payment_type'],
                            bank_account_number=bank_account_number,
                            credit_account_number=credit_account_number,
                            actual_master_category_id=request.POST['actual_master_category_id'],
                            actual_category_id=request.POST['actual_category_id'],
                            actual_subcategory_id=request.POST['actual_subcategory_id'],
                            actual_expense=float(int(request.POST['actual_expense']) / int(request.POST['syncing_month'])),
                            expense_date=request.POST['actual_expense_date'],
                            syncing_amount=request.POST['actual_expense'],
                            syncing_month=request.POST['syncing_month'],
                            actual_income=0,
                        )
                    else:
                        ActualexpenseModel.objects.create(
                            user_id=request.session['user_id'],
                            is_month=str(month).replace(" ","") +str(int(current_year) + 1),
                            payment_category=request.POST['payment_category'],
                            payment_type=request.POST['payment_type'],
                            bank_account_number=bank_account_number,
                            credit_account_number=credit_account_number,
                            actual_master_category_id=request.POST['actual_master_category_id'],
                            actual_category_id=request.POST['actual_category_id'],
                            actual_subcategory_id=request.POST['actual_subcategory_id'],
                            actual_expense=float(int(request.POST['actual_expense']) / int(request.POST['syncing_month'])),
                            expense_date=request.POST['actual_expense_date'],
                            syncing_amount=request.POST['actual_expense'],
                            syncing_month=request.POST['syncing_month'],
                            actual_income=0,
                        )
            else:
                for month in months:
                    ActualexpenseModel.objects.create(
                                user_id=request.session['user_id'],
                                is_month=str(month).replace(" ","") +str(int(current_year)),
                                payment_category=request.POST['payment_category'],
                                payment_type=request.POST['payment_type'],
                                bank_account_number=bank_account_number,
                                credit_account_number=credit_account_number,
                                actual_master_category_id=request.POST['actual_master_category_id'],
                                actual_category_id=request.POST['actual_category_id'],
                                actual_subcategory_id=request.POST['actual_subcategory_id'],
                                actual_expense=float(int(request.POST['actual_expense'])),
                                expense_date=request.POST['actual_expense_date'],
                                syncing_amount=request.POST['actual_expense'],
                                syncing_month=request.POST['syncing_month'],
                                actual_income=0,
                            )
         else:
            ActualexpenseModel.objects.create(
                user_id=request.session['user_id'],
                is_month=request.POST['is_month'],
                payment_category=request.POST['payment_category'],
                payment_type=request.POST['payment_type'],
                bank_account_number=request.POST['bank_account_number'],
                credit_account_number=request.POST['credit_account_number'],
                #  Temporary category
                actual_master_category_id=1,
                actual_category_id=1,
                actual_subcategory_id=1,
                actual_expense=request.POST['actual_expense'],
                actual_income=request.POST['actual_income'],
                syncing_amount=0,
                syncing_month=0,
                expense_date = request.POST['actual_income_date']
            )
            messages.add_message(request, messages.SUCCESS, 'expense data inerted')
         return redirect('view_expense',request.POST['is_month'])

def view_expense(request,month):
    actualexpensedata=ActualexpenseModel.objects.filter(user_id=request.session['user_id'],is_month=month).values()
    for newactualexpensedata in actualexpensedata:
        if (newactualexpensedata['payment_category']=='income'):
            newactualexpensedata['master_category'] = '-'
            newactualexpensedata['category_name'] = '-'
            newactualexpensedata['subcategory_name'] = '-'
            newactualexpensedata['type'] = 'Income'
            newactualexpensedata['actual_expense'] = "{:.0f}".format(float(newactualexpensedata['actual_income']))
            # newactualexpensedata['actual_expense'] = newactualexpensedata['actual_income']
        else:
            mastercategory=BudgetcategoriesModel.objects.get(id=newactualexpensedata['actual_master_category_id'])
            newactualexpensedata['master_category']=mastercategory.category_name
            category=BudgetsubcategoriesModel.objects.get(id=newactualexpensedata['actual_category_id'])
            newactualexpensedata['category_name']=category.subcategory_name
            subcategory=BudgetlastcategoriesModel.objects.get(id=newactualexpensedata['actual_subcategory_id'])
            newactualexpensedata['subcategory_name']=subcategory.last_category_name
            newactualexpensedata['type']='Expense'
    data = {'actualexpenses_page': 'active','month':month,'actualexpensedata':actualexpensedata}
    return render(request, 'user_template/actualexpenses/view_expense.html', data)

def deleteexpense(request):
    if request.method=='POST':
        month_name=request.POST['month_name']
        expenseid=request.POST['expenseid']
        data=ActualexpenseModel.objects.get(id=expenseid)
        data.delete()
        messages.add_message(request, messages.SUCCESS, 'expense data deleted')
        return redirect('view_expense', month_name)

def getcategory(request):
    if request.method=='POST':
        actual_master_category=request.POST['actual_master_category']
        category=BudgetsubcategoriesModel.objects.filter(budget_category_id=actual_master_category)
        data=[]
        one='<select class="form-control" id="actual_category" name="actual_category_id" onchange="GetsubcategoryFunction()"><option>--select category--</option>'
        for newcategory in category:
            option='<option value="'+str(newcategory.id)+'" >'+newcategory.subcategory_name+'</option>'
            data.append(option)
        three='</select>'
        finaldata=one+str(data)+three
        return HttpResponse(finaldata)

def getsubcategory(request):
    if request.method=='POST':
        actual_category=request.POST['actual_category']
        subcategory=BudgetlastcategoriesModel.objects.filter(budget_subcategory_id=actual_category)
        data=[]
        one='<select class="form-control" id="actual_subcategory" name="actual_subcategory_id"><option>--select subcategory--</option>'
        for newsubcategory in subcategory:
            option='<option value="'+str(newsubcategory.id)+'" >'+newsubcategory.last_category_name+'</option>'
            data.append(option)
        three='</select>'
        finaldata=one+str(data)+three
        return HttpResponse(finaldata)























