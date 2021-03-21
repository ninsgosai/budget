from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver

from adminusers.models import AdminuserModel
from adminbudgetcategories.models import BudgetcategoriesModel,BudgetsubcategoriesModel,BudgetlastcategoriesModel
from admintaxcategory.models import TaxcategoryModel
from adminsavingcategory.models import SavingcategoryModel,IncomecategoryModel

class IncomeModel(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(AdminuserModel, on_delete=models.CASCADE)
    # income_category = models.ForeignKey(IncomecategoryModel, on_delete=models.CASCADE)
    income_category = models.CharField(max_length=255)
    month= models.CharField(max_length=255)
    name= models.CharField(max_length=255)
    income= models.CharField(max_length=255)
    is_row= models.CharField(max_length=255,default="")
    created_date = models.DateTimeField(auto_now_add=True)

class TaxModel(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(AdminuserModel, on_delete=models.CASCADE)
    month = models.CharField(max_length=255,default="")
    tax_category= models.ForeignKey(TaxcategoryModel, on_delete=models.CASCADE , blank = True)
    member_name= models.CharField(max_length=255)
    tax_per= models.CharField(max_length=255)
    tax_row = models.CharField(max_length=255, default="")
    tax_amt = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)

class SavingsModel(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(AdminuserModel, on_delete=models.CASCADE)
    month = models.CharField(max_length=255,default="")
    saving_category= models.ForeignKey(SavingcategoryModel, on_delete=models.CASCADE)
    family_member_name= models.CharField(max_length=255)
    saving_per= models.CharField(max_length=255)
    saving_row = models.CharField(max_length=255, default="")
    saving_amt = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)

class ExpensesModel(models.Model):
    id = models.AutoField(primary_key=True)
    syncing_amount = models.FloatField(default=0)
    syncing_month = models.IntegerField(default=0)
    user = models.ForeignKey(AdminuserModel, on_delete=models.CASCADE)
    month = models.CharField(max_length=255,default="")
    master_category= models.ForeignKey(BudgetcategoriesModel, on_delete=models.CASCADE)
    category= models.ForeignKey(BudgetsubcategoriesModel, on_delete=models.CASCADE)
    subcategory= models.ForeignKey(BudgetlastcategoriesModel, on_delete=models.CASCADE)
    total_expenses= models.FloatField(default=0)
    expense_amt = models.CharField(max_length=255,default="")
    created_date = models.DateTimeField(auto_now_add=True)