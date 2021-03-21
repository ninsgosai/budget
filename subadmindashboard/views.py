from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
import os

from subadminauth.middlewares import checksubadminfunction
from adminusers.models import SubadminauthModel

@checksubadminfunction
def subadmindashboard(request):
    pk = request.session.get('subadmin_id')
    subadmins = SubadminauthModel.objects.get(pk=pk)
    data={'subadmin_dashboard_page':'active','subadmindata':subadmins}
    return render(request,'subadmin_template/dashboard/dashboard.html',data)

#password change
def checkuserpassword(request):
    if request.method=='POST':
        current_password=request.POST['current_password']
        userdata=SubadminauthModel.objects.get(id=request.session['subadmin_id'])
        if userdata.subadmin_password==current_password:
            return HttpResponse('1')
        else:
            return HttpResponse('0')

def updateuserpassword(request):
    if request.method=='POST':
        subadmin_password=request.POST['subadmin_password']
        data=SubadminauthModel.objects.get(id=request.session['subadmin_id'])
        data.subadmin_password=request.POST['subadmin_password']
        data.save()
        return HttpResponse('1')

#profile
@checksubadminfunction
def subadminprofile(request):
    subadmindata=SubadminauthModel.objects.get(id=request.session['subadmin_id'])
    data={'subadmin_dashboard_page':'active','subadmindata':subadmindata}
    return render(request,'subadmin_template/dashboard/profile.html',data)

def updatesubadminprofile(request):
    if request.method=='POST':
        if request.FILES['subadmin_photo']:
            data=SubadminauthModel.objects.get(id=request.session['subadmin_id'])
            data.subadmin_email=request.POST['subadmin_email']
            data.subadmin_name=request.POST['subadmin_name']
            data.subadmin_password=request.POST['subadmin_password']
            data.profile_pic=request.FILES['subadmin_photo']
        else:
            data=SubadminauthModel.objects.get(id=request.session['subadmin_id'])
            data.subadmin_email=request.POST['subadmin_email']
            data.subadmin_name=request.POST['subadmin_name']
            data.subadmin_password=request.POST['subadmin_password']
        data.save()
        messages.add_message(request, messages.SUCCESS, 'profile updated successfully')
        return redirect('subadminprofile')
