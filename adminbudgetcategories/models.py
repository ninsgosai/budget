from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver

class BudgetcategoriesModel(models.Model):
    id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=255,unique=True)
    created_date = models.DateTimeField(auto_now_add=True)

class BudgetsubcategoriesModel(models.Model):
    id = models.AutoField(primary_key=True)
    budget_category = models.ForeignKey(BudgetcategoriesModel, on_delete=models.CASCADE)
    subcategory_name = models.CharField(max_length=255,unique=True)
    created_date = models.DateTimeField(auto_now_add=True)

class BudgetlastcategoriesModel(models.Model):
    id = models.AutoField(primary_key=True)
    budget_subcategory = models.ForeignKey(BudgetsubcategoriesModel, on_delete=models.CASCADE)
    last_category_name = models.CharField(max_length=255,default="",null=True,blank=True)
    created_date = models.DateTimeField(auto_now_add=True)