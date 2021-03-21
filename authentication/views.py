from django.shortcuts import render,redirect
from django.template import loader
from django.http import HttpResponse
from django.contrib import messages
import os
from adminauth.models import AdminauthModel
from adminusers.models import AdminuserModel
from adminusers.models import AdminuserModel,SubadminauthModel

def authentication(request):
    if request.method=='POST':
        if request.POST['log_type']=="1":
            if AdminuserModel.objects.filter(email=request.POST['email'],password=request.POST['password'],status=True).exists():
                userdata=AdminuserModel.objects.get(email=request.POST['email'],password=request.POST['password'])
                request.session['user_id']=userdata.id
                request.session['username']=userdata.username
                request.session['email']=userdata.email
                if userdata.profile_pic:
                    request.session['user_photo']=userdata.profile_pic.url
                messages.add_message(request, messages.SUCCESS, 'login successfull')
                return redirect('dashboard')
            else:
                if AdminuserModel.objects.filter(email=request.POST['email'],password=request.POST['password'],status=False).exists():
                    messages.add_message(request, messages.SUCCESS, 'You are Blocked by admin Please Contact Admin For Activate')
                else:
                    messages.add_message(request, messages.SUCCESS, 'wrong email or password')
                return redirect('authentication')
        elif request.POST['log_type']=="2":
            if SubadminauthModel.objects.filter(subadmin_email=request.POST['email'],subadmin_password=request.POST['password'],status=True).exists():
                subadmindata=SubadminauthModel.objects.get(subadmin_email=request.POST['email'],subadmin_password=request.POST['password'])
                request.session['subadmin_id']=subadmindata.id
                request.session['subadmin_name']=subadmindata.subadmin_name
                request.session['subadmin_email']=subadmindata.subadmin_email
                messages.add_message(request, messages.SUCCESS, 'login successfull')
                return redirect('subadmindashboard')
            else:
                if SubadminauthModel.objects.filter(subadmin_email=request.POST['email'],subadmin_password=request.POST['password'],status=False).exists():
                    messages.add_message(request, messages.SUCCESS, 'You are Blocked by admin Please Contact Admin For Activate')
                else:
                    messages.add_message(request, messages.SUCCESS, 'wrong email or password')
                return redirect('authentication')

        elif request.POST['log_type']=="3":
            if AdminauthModel.objects.filter(admin_email=request.POST['email'],admin_password=request.POST['password']).exists():
                admindata=AdminauthModel.objects.get(admin_email=request.POST['email'],admin_password=request.POST['password'])
                request.session['admin_id']=admindata.id
                request.session['admin_email']=admindata.admin_email
                if admindata.profile_pic:
                    request.session['profile_pic']=admindata.profile_pic.url
                return redirect('admindashboard')
            else:
                messages.add_message(request, messages.SUCCESS, 'wrong email or password')
                return redirect('authentication')

    else:
            data={'user_auth_page':'active'}
            return render(request,'user_template/authentication/login.html',data)

def userlogout(request):
    del request.session['user_id']
    del request.session['username']
    del request.session['email']
    if 'user_photo' in request.session and request.session['user_photo']:
        del request.session['user_photo']
    return redirect('authentication')