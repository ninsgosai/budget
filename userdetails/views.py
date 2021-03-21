from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
import os

from authentication.middlewares import checkuserauthfunction
from adminusers.models import AdminuserModel,UserbankdetailModel,UsercreditcardModel,UserotherloanModel,UserFamilyModel
from adminbudgetcategories.models import BudgetcategoriesModel

#bank details
@checkuserauthfunction
def userdetails(request):
    bankdetails=UserbankdetailModel.objects.filter(user_id=request.session['user_id'])
    data = {'userdetail_page': 'active','bankdetails':bankdetails}
    return render(request, 'user_template/userdetails/bankdetails.html', data)

def insertbankdetails(request):
    if request.method=='POST':
        UserbankdetailModel.objects.create(
            user_id=request.session['user_id'],
            bank_name=request.POST['bank_name'],
            account_number=request.POST['account_number'],
            od_token=request.POST['od_token'],
            current_balance=request.POST['current_balance'],
            intrest_time_period=request.POST['intrest_time_period'],
            intrest_type=request.POST['intrest_type'],
            intrest_rate=request.POST['intrest_rate'],
            is_form_two=1,
        )
        bankdetails=UserbankdetailModel.objects.filter(user_id=request.session['user_id'])
        data=[]
        for newbankdetails in bankdetails:
            bankdata='<button  style="background-color: white;color:#F9A524;" type="button" class="mb-1 btn btn-primary">xxxx xxxx xxxx '+newbankdetails.account_number+'&nbsp;<a data-bank_id="'+str(newbankdetails.id)+'" id="delete_bank_details"><i class="far fa-window-close" style="color:red;"></i></a>&nbsp;<a><i class="fas fa-edit" style="color:#0f9e0f;"></i></a></button>&nbsp;&nbsp;'
            data.append(bankdata)
        return HttpResponse(data)

def deletebankdetails(request):
    if request.method=='POST':
        bank_id=request.POST['bank_id']
        data=UserbankdetailModel.objects.get(id=bank_id)
        data.delete()
        bankdetails = UserbankdetailModel.objects.filter(user_id=request.session['user_id'])
        data = []
        for newbankdetails in bankdetails:
            bankdata = '<button  style="background-color: white;color:#F9A524;" type="button" class="mb-1 btn btn-primary">xxxx xxxx xxxx ' + newbankdetails.account_number + '&nbsp;<a data-bank_id="'+str(newbankdetails.id)+'" id="delete_bank_details"><i class="far fa-window-close" style="color:red;"></i></a>&nbsp;<a><i class="fas fa-edit" style="color:#0f9e0f;"></i></a></button>&nbsp;&nbsp;'
            data.append(bankdata)
        return HttpResponse(data)

def fetchbankdetails(request,id):
    bankdata=UserbankdetailModel.objects.get(id=id)
    data = {'userdetail_page': 'active', 'bankdata': bankdata}
    return render(request, 'user_template/userdetails/edit_bankdetails.html', data)

def updatebankdetails(request):
    if request.method=='POST':
        bank_hidden_id=request.POST['bank_hidden_id']
        bankdata=UserbankdetailModel.objects.get(id=bank_hidden_id)
        bankdata.bank_name=request.POST['bank_name']
        bankdata.account_number=request.POST['account_number']
        bankdata.od_token=request.POST['od_token']
        bankdata.current_balance=request.POST['current_balance']
        bankdata.intrest_time_period=request.POST['intrest_time_period']
        bankdata.intrest_type=request.POST['intrest_type']
        bankdata.intrest_rate=request.POST['intrest_rate']
        bankdata.save()
        return HttpResponse('1')


# credit card functions
@checkuserauthfunction
def creditcarddetails(request):
    allcreditcard=UsercreditcardModel.objects.filter(user_id=request.session['user_id'])
    data = {'userdetail_page': 'active','allcreditcard':allcreditcard}
    return render(request, 'user_template/userdetails/creditcard_details.html', data)

def insertcreditcarddetails(request):
    if request.method=='POST':
        UsercreditcardModel.objects.create(
            user_id=request.session['user_id'],
            credit_card_number=request.POST['credit_card_number'],
            credit_limit=request.POST['credit_limit'],
            charges_and_fees=request.POST['charges_and_fees'],
            due_date=request.POST['due_date'],
            overdue=request.POST['overdue'],
            intrest_on_payable=request.POST['intrest_on_payable'],
            payment_made=request.POST['payment_made'],
            is_form_three=1,
        )
        creditcard = UsercreditcardModel.objects.filter(user_id=request.session['user_id'])
        data = []
        for newcreditcard in creditcard:
            creditdata = '<button  style="background-color: white;color:#F9A524;" type="button" class="mb-1 btn btn-primary">xxxx xxxx xxxx ' + newcreditcard.credit_card_number + '&nbsp;<a data-credit_card_id="'+str(newcreditcard.id)+'" id="delete_credit_card"><i class="far fa-window-close" style="color:red;"></i></a>&nbsp;<a><i class="fas fa-edit" style="color:#0f9e0f;"></i></a></button>&nbsp;&nbsp;'
            data.append(creditdata)
        return HttpResponse(data)

def deletecreditcard(request):
    if request.method=='POST':
        credit_card_id=request.POST['credit_card_id']
        data=UsercreditcardModel.objects.get(id=credit_card_id)
        data.delete()
        creditcard = UsercreditcardModel.objects.filter(user_id=request.session['user_id'])
        data = []
        for newcreditcard in creditcard:
            creditdata = '<button  style="background-color: white;color:#F9A524;" type="button" class="mb-1 btn btn-primary">xxxx xxxx xxxx ' + newcreditcard.credit_card_number + '&nbsp;<a data-credit_card_id="'+str(newcreditcard.id)+'" id="delete_credit_card"><i class="far fa-window-close" style="color:red;"></i></a>&nbsp;<a><i class="fas fa-edit" style="color:#0f9e0f;"></i></a></button>&nbsp;&nbsp;'
            data.append(creditdata)
        return HttpResponse(data)

def edit_caredit_card_details(request,id):
    creditdata=UsercreditcardModel.objects.get(id=id)
    data = {'userdetail_page': 'active', 'creditdata': creditdata}
    return render(request, 'user_template/userdetails/edit_creditcard_details.html', data)

def updatecreditcard(request):
    if request.method=='POST':
        credit_hidden_val=request.POST['credit_hidden_val']
        creditdata=UsercreditcardModel.objects.get(id=credit_hidden_val)
        creditdata.credit_card_number=request.POST['credit_card_number']
        creditdata.credit_limit=request.POST['credit_limit']
        creditdata.charges_and_fees=request.POST['charges_and_fees']
        creditdata.due_date=request.POST['due_date']
        creditdata.overdue=request.POST['overdue']
        creditdata.intrest_on_payable=request.POST['intrest_on_payable']
        creditdata.payment_made=request.POST['payment_made']
        creditdata.save()
        return HttpResponse('1')


#other loans
@checkuserauthfunction
def otherloans(request):
    otherloansdata=UserotherloanModel.objects.filter(user_id=request.session['user_id'])
    data = {'userdetail_page': 'active','otherloansdata':otherloansdata}
    return render(request, 'user_template/userdetails/otherloans.html', data)

def insertotherloans(request):
    if request.method=='POST':
        UserotherloanModel.objects.create(
            user_id=request.session['user_id'],
            loan_name=request.POST['loan_name'],
            loan_amount=request.POST['loan_amount'],
            roi_percentage_type=request.POST['roi_percentage_type'],
            roi_percentage=request.POST['roi_percentage'],
            other_due_date=request.POST['other_due_date'],
            other_intrest_type=request.POST['other_intrest_type'],
            loan_duration=request.POST['loan_duration'],
            is_form_four=1,
        )
        loans = UserotherloanModel.objects.filter(user_id=request.session['user_id'])
        data = []
        for newloans in loans:
            creditdata = '<button  style="background-color: white;color:#F9A524;" type="button" class="mb-1 btn btn-primary">xxxx xxxx xxxx ' + newloans.loan_name + '&nbsp;<a><i class="far fa-window-close" style="color:red;"></i></a>&nbsp;<a><i class="fas fa-edit" style="color:#0f9e0f;"></i></a></button>&nbsp;&nbsp;'
            data.append(creditdata)
        return HttpResponse(data)

def deleteotherloans(request,id):
    data=UserotherloanModel.objects.get(id=id)
    data.delete()
    return redirect('otherloans')

def editotherloans(request,id):
    loandata=UserotherloanModel.objects.get(id=id)
    data = {'userdetail_page': 'active', 'loandata': loandata}
    return render(request, 'user_template/userdetails/edit_otherloans.html', data)

def updateotherloans(request):
    if request.method=='POST':
        other_loan_hidden_id=request.POST['other_loan_hidden_id']
        data=UserotherloanModel.objects.get(id=other_loan_hidden_id)
        data.loan_name=request.POST['loan_name']
        data.loan_amount=request.POST['loan_amount']
        data.roi_percentage_type=request.POST['roi_percentage_type']
        data.roi_percentage=request.POST['roi_percentage']
        data.other_due_date=request.POST['other_due_date']
        data.other_intrest_type=request.POST['other_intrest_type']
        data.loan_duration=request.POST['loan_duration']
        data.save()
        return HttpResponse('1')

# By Ninad 
def familydetails(request):
    family = UserFamilyModel.objects.filter(adminusermodel=request.session['user_id'])
    return render(request,'user_template/userdetails/family.html',{'userdata':family})
def addfamilydetails(request):
    if request.method=="POST":
        userfamilymodal = UserFamilyModel()
        userfamilymodal.username = request.POST['username']
        adminuser = AdminuserModel.objects.get(pk=int(request.session['user_id']))
        userfamilymodal.adminusermodel = adminuser
        userfamilymodal.age = request.POST['age']
        userfamilymodal.gender = request.POST['gender']
        userfamilymodal.email = request.POST['email']
        userfamilymodal.mobile = request.POST['mobile']
        userfamilymodal.address =  request.POST['address']
        userfamilymodal.income = request.POST['income']
        userfamilymodal.goal = request.POST['goal']
        userfamilymodal.save()
        messages.add_message(request, messages.SUCCESS, 'family Member Added successfully')
        family = UserFamilyModel.objects.filter(adminusermodel=request.session['user_id'])


        return render(request,'user_template/userdetails/family.html',{'userdata':family})

    return render(request,'user_template/userdetails/addfamily.html')
def updatefamilydetails(request,pk):
    family = UserFamilyModel.objects.get(pk=pk)
    if request.method=="POST":
        userfamilymodal = UserFamilyModel.objects.get(id=pk)
        userfamilymodal.username = request.POST['username']
        adminuser = AdminuserModel.objects.get(pk=int(request.session['user_id']))
        userfamilymodal.adminusermodel = adminuser
        userfamilymodal.age = request.POST['age']
        userfamilymodal.gender = request.POST['gender']
        userfamilymodal.email = request.POST['email']
        userfamilymodal.mobile = request.POST['mobile']
        userfamilymodal.address =  request.POST['address']
        userfamilymodal.income = request.POST['income']
        userfamilymodal.goal = request.POST['goal']
        userfamilymodal.save()
        messages.add_message(request, messages.SUCCESS, 'family Member Updated successfully')
        family = UserFamilyModel.objects.filter(adminusermodel=request.session['user_id'])
        return render(request,'user_template/userdetails/family.html',{'userdata':family})
    return render(request,'user_template/userdetails/editfamily.html',{'userdata':family})
def deletefamily(request):
    if request.method=='POST':
        userid=request.POST['userid']
        data=UserFamilyModel.objects.get(id=userid)
        data.delete()
        messages.add_message(request, messages.SUCCESS, 'user deleted successfully')
        return redirect('familydetails')











