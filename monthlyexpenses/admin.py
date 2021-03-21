from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(IncomeModel)
admin.site.register(TaxModel)
admin.site.register(SavingsModel)
admin.site.register(ExpensesModel)