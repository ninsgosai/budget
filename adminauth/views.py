from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
import os

from adminauth.models import AdminauthModel

def adminauth(request):
      if request.method=='POST':
         if AdminauthModel.objects.filter(admin_email=request.POST['admin_email'],admin_password=request.POST['admin_password']).exists():
            admindata=AdminauthModel.objects.get(admin_email=request.POST['admin_email'],admin_password=request.POST['admin_password'])
            request.session['admin_id']=admindata.id
            request.session['admin_email']=admindata.admin_email
            request.session['profile_pic']=admindata.profile_pic.url
            return redirect('admindashboard')
         else:
             messages.add_message(request, messages.SUCCESS, 'wrong email or password')
             return redirect('authentication')
      else:
        data={'admin_login_page':'active'}
        return render(request, 'admin_template/authentication/login.html', data)


def adminlogout(request):
    del request.session['admin_id']
    del request.session['admin_email']
    if 'profile_pic' in request.session and request.session['profile_pic']:
      del request.session['profile_pic']
    return redirect('authentication')