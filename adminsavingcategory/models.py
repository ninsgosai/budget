from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from adminusers.models import AdminuserModel

class SavingcategoryModel(models.Model):
    id = models.AutoField(primary_key=True)
    saving_category_name = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)

class IncomecategoryModel(models.Model):
    id = models.AutoField(primary_key=True)
    income_category_name = models.CharField(max_length=255)
    admin = models.ForeignKey(AdminuserModel, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)