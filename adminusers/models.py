from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from datetime import date

from adminauth.models import AdminauthModel
from adminusers import *

class SubadminauthModel(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.ForeignKey(AdminauthModel, on_delete=models.CASCADE)
    subadmin_email = models.EmailField(max_length=255)
    subadmin_name = models.CharField(max_length=255,default="")
    last_name = models.CharField(max_length=255,default="",blank=True,null=True)
    subadmin_password = models.CharField(max_length=255)
    profile_pic = models.ImageField('Profile Pic', upload_to='profile_pic/',null=True)
    status =models.BooleanField(default=True)
    
    created_date = models.DateTimeField(auto_now_add=True)

class AdminuserModel(models.Model):
    id = models.AutoField(primary_key=True)
    subadmin = models.ForeignKey(SubadminauthModel, on_delete=models.CASCADE, null=True, blank=True, default="")
    username = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    password = models.CharField(max_length=255 , default="")
    age = models.DateField(blank=True, null=True)
    # age = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    mobile = models.CharField(max_length=255)
    address =  models.TextField()                                               # Store Street 
    address_city =  models.TextField(null=True,blank=True)                      # Store City 
    address_country =  models.TextField(null=True,blank=True)                   # Store Country 
    address_pincode =  models.TextField(null=True,blank=True)                   # Store pincode 
    # income = models.CharField(max_length=255)
    # goal = models.TextField()
    subscription_from_time = models.DateField()
    subscription_to_time = models.DateField()
    months = models.CharField(max_length=255,default="")
    profile_pic = models.ImageField('Profile Pic', upload_to='profile_pic/',null=True)
    status =models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def dateFormat_subscription_from_time(self):
        return str(self.subscription_from_time)

    def dateFormat_subscription_to_time(self):
        return str(self.subscription_to_time)

    def dateFormat_birthdate(self):
        return str(self.age)

class UserFamilyModel(models.Model):
    id = models.AutoField(primary_key=True)
    adminusermodel = models.ForeignKey(AdminuserModel, on_delete=models.CASCADE,default="")
    username = models.CharField(max_length=255)
    age = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    mobile = models.CharField(max_length=255)
    address =  models.TextField()
    income = models.CharField(max_length=255)
    goal = models.TextField()
    # subscription_from_time = models.DateField()
    # subscription_to_time = models.DateField()
    # months = models.CharField(max_length=255,default="")
    created_date = models.DateTimeField(auto_now_add=True)

    def dateFormat_birthdate(self):
        return str(self.age)

class UserbankdetailModel(models.Model):
    user= models.ForeignKey(AdminuserModel, on_delete=models.CASCADE)
    bank_name = models.CharField(max_length=255)
    account_number = models.CharField(max_length=255)
    od_token = models.CharField(max_length=255)
    current_balance = models.CharField(max_length=255)
    intrest_time_period = models.CharField(max_length=255)
    intrest_type = models.CharField(max_length=255)
    intrest_rate = models.CharField(max_length=255)
    is_form_two = models.CharField(max_length=255)

class UsercreditcardModel(models.Model):
    user= models.ForeignKey(AdminuserModel, on_delete=models.CASCADE)
    credit_card_number = models.CharField(max_length=255)
    credit_limit = models.CharField(max_length=255)
    charges_and_fees = models.CharField(max_length=255)
    due_date = models.CharField(max_length=255)
    overdue = models.CharField(max_length=255)
    intrest_on_payable = models.CharField(max_length=255)
    payment_made = models.CharField(max_length=255)
    is_form_three = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)

class UserotherloanModel(models.Model):
    user= models.ForeignKey(AdminuserModel, on_delete=models.CASCADE)
    loan_name = models.CharField(max_length=255)
    loan_amount = models.CharField(max_length=255)
    roi_percentage_type = models.CharField(max_length=255)
    roi_percentage = models.CharField(max_length=255)
    other_due_date = models.CharField(max_length=255)
    other_intrest_type = models.CharField(max_length=255)
    loan_duration = models.CharField(max_length=255)
    is_form_four = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)

class UserincomeCategory(models.Model):
    id = models.AutoField(primary_key=True)
    income_category_name = models.CharField(max_length=255)
    admin = models.ForeignKey(AdminuserModel, on_delete=models.CASCADE)


