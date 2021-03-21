from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
import os

from authentication.middlewares import checkuserauthfunction
from adminusers.models import AdminuserModel

@checkuserauthfunction
def dashboard(request):
    userdata=AdminuserModel.objects.get(id=request.session['user_id'])
    data={'dashboard_page':'active','userdata':userdata}
    return render(request,'user_template/dashboard/dashboard.html',data)

def checkuserpassword(request):
    if request.method=='POST':
        current_password=request.POST['current_password']
        userdata=AdminuserModel.objects.get(id=request.session['user_id'])
        if userdata.password==current_password:
            return HttpResponse('1')
        else:
            return HttpResponse('0')

def updateuserpassword(request):
    if request.method=='POST':
        password=request.POST['password']
        data=AdminuserModel.objects.get(id=request.session['user_id'])
        data.password=request.POST['password']
        data.save()
        return HttpResponse('1')

def userprofile(request):
    userdata=AdminuserModel.objects.get(id=request.session['user_id'])
    data={'dashboard_page':'active','userdata':userdata}
    return render(request,'user_template/dashboard/profile.html',data)

def updateprofile(request):
    if request.method=='POST':
        data=AdminuserModel.objects.get(id=request.session['user_id'])
        if 'user_photo' in request.FILES and request.FILES['user_photo']:
            data.username=request.POST['user_name']
            data.lastname=request.POST['last_name']
            data.password=request.POST['user_password']
            data.age=request.POST['user_birthdate']
            data.gender=request.POST['user_gender']
            data.mobile=request.POST['user_mobile']
            data.address=request.POST['user_street']
            data.address_city=request.POST['user_city']
            data.address_country=request.POST['user_country']
            data.address_pincode=request.POST['user_pincode']
            data.profile_pic=request.FILES['user_photo']
            data.save()
            data=AdminuserModel.objects.get(id=request.session['user_id'])
            if 'user_photo' in request.session and request.session['user_photo']:
                del request.session['user_photo']
            request.session['user_photo']=data.profile_pic.url
        else:
            data.username=request.POST['user_name']
            data.lastname=request.POST['last_name']
            data.password=request.POST['user_password']
            data.age=request.POST['user_birthdate']
            data.gender=request.POST['user_gender']
            data.mobile=request.POST['user_mobile']
            data.address=request.POST['user_street']
            data.address_city=request.POST['user_city']
            data.address_country=request.POST['user_country']
            data.address_pincode=request.POST['user_pincode']
            data.save()
        messages.add_message(request, messages.SUCCESS, 'profile updated successfully')
    return redirect('userprofile')
    

















