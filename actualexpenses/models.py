from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver

from adminbudgetcategories.models import BudgetcategoriesModel,BudgetsubcategoriesModel,BudgetlastcategoriesModel

class ActualexpenseModel(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    is_month = models.CharField(max_length=255)
    payment_category = models.CharField(max_length=255)
    payment_type = models.CharField(max_length=255)
    bank_account_number = models.CharField(max_length=255)
    credit_account_number = models.CharField(max_length=255,default="")
    actual_master_category = models.ForeignKey(BudgetcategoriesModel, on_delete=models.CASCADE)
    actual_category = models.ForeignKey(BudgetsubcategoriesModel, on_delete=models.CASCADE)
    actual_subcategory = models.ForeignKey(BudgetlastcategoriesModel, on_delete=models.CASCADE)
    actual_expense = models.CharField(max_length=255)
    actual_income = models.CharField(max_length=255,default="")
    syncing_amount = models.FloatField(default=0)
    syncing_month = models.IntegerField(default=0)
    expense_date = models.DateTimeField()
    created_date = models.DateTimeField(auto_now_add=True)
