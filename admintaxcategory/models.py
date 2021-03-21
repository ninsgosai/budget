from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from adminusers.models import AdminuserModel

class TaxcategoryModel(models.Model):
    id = models.AutoField(primary_key=True)
    tax_category_name = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)

class Goal(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.ForeignKey(AdminuserModel, on_delete=models.CASCADE,default="")
    goal = models.CharField(max_length=500,default="",null=True,blank=True)
    goal_amount = models.IntegerField(default=0,blank=True,null=True)
    start_date = models.DateField(null=True,blank=True)
    deadline_date = models.DateField(null=True,blank=True)
    status = models.BooleanField(default=False)
    month= models.CharField(max_length=255,default="",blank=True,null=True)
    created_date = models.DateTimeField(auto_now_add=True)