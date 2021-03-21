from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
import os
from datetime import datetime, timedelta

from adminauth.middlewares import checkadminauth
from adminauth.models import AdminauthModel
from adminusers.models import AdminuserModel,SubadminauthModel

#admin functions
@checkadminauth
def admindashboard(request):
    subadmincount=SubadminauthModel.objects.filter(status=True).count()
    usercount=AdminuserModel.objects.filter(status=True).count()
    totalsubadmincount=SubadminauthModel.objects.filter(status=True).count()
    totalusercount=AdminuserModel.objects.filter(status=True).count()
    totalusers = totalsubadmincount + totalusercount
    # subadmin=SubadminauthModel.objects.all()[:5]
    # users=AdminuserModel.objects.all()[:5]
    subadmin=SubadminauthModel.objects.filter(created_date__gte=datetime.now()-timedelta(days=7))
    users=AdminuserModel.objects.filter(created_date__gte=datetime.now()-timedelta(days=7))

    data={'dashboard_page':'active',
          'subadmincount':subadmincount,
          'usercount':usercount,
          'subadmin':subadmin,
          'totalusercount':totalusers,
          'users':users
          }
    return render(request,'admin_template/dashboard/dashboard.html',data)

def checkpassword(request):
    if request.method=='POST':
        current_password=request.POST['current_password']
        admindata=AdminauthModel.objects.get(id=request.session['admin_id'])
        if admindata.admin_password==current_password:
            return HttpResponse('1')
        else:
            return HttpResponse('0')

def updatepassword(request):
    if request.method=='POST':
        admindata=AdminauthModel.objects.get(id=request.session['admin_id'])
        if request.FILES['profile_pic']:
            admindata.admin_password=request.POST['admin_password']
            admindata.profile_pic=request.FILES['profile_pic']
        else:
            admindata.admin_password=request.POST['admin_password']
        
        admindata.save()
        return HttpResponse('1')

def adminprofile(request):
    if request.method=='POST':
        data=AdminauthModel.objects.get(id=request.session['admin_id'])
        if request.FILES['profile_pic']:
            data.admin_email=request.POST['admin_email']
            data.admin_password=request.POST['admin_password']
            data.profile_pic=request.FILES['profile_pic']
            data.save()
            if 'profile_pic' in request.session and request.session['profile_pic']:
                del request.session['profile_pic']
            data=AdminauthModel.objects.get(id=request.session['admin_id'])
            request.session['profile_pic']=data.profile_pic.url

        else:
            data.admin_email=request.POST['admin_email']
            data.admin_password=request.POST['admin_password']
            data.save()
        messages.add_message(request, messages.SUCCESS, 'profile updated successfully')
        return redirect('adminprofile')
    else:
        admindata=AdminauthModel.objects.get(id=request.session['admin_id'])
        data = {'dashboard_page': 'active','admindata':admindata}
        return render(request, 'admin_template/dashboard/profile.html', data)



