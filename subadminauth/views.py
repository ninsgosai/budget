from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
import os

from adminusers.models import AdminuserModel,SubadminauthModel

def subadminauth(request):
    if request.method=='POST': 
        if SubadminauthModel.objects.filter(subadmin_email=request.POST['subadmin_email'],subadmin_password=request.POST['subadmin_password']).exists():
            subadmindata=SubadminauthModel.objects.get(subadmin_email=request.POST['subadmin_email'],subadmin_password=request.POST['subadmin_password'])
            request.session['subadmin_id']=subadmindata.id
            request.session['subadmin_name']=subadmindata.subadmin_name
            request.session['subadmin_email']=subadmindata.subadmin_email
            messages.add_message(request, messages.SUCCESS, 'login successfull')
            return redirect('subadmindashboard')
        else:
            messages.add_message(request, messages.SUCCESS, 'wrong email or password')
            return redirect('authentication')
    else:
        data={'subadmin_auth_page':'active'}
        return render(request,'subadmin_template/authentication/login.html',data)


def subadminlogout(request):
    del request.session['subadmin_id']
    del request.session['subadmin_name']
    del request.session['subadmin_email']
    return redirect('authentication')
