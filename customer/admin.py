from django.contrib import admin
from .models import *

class AdminCustomer(admin.ModelAdmin):
    list_display=['account_no','name','balance']

class AdminTransfer(admin.ModelAdmin):
    list_display=['from_account','to_account','amount','updated_at']
# Register your models here.
admin.site.register(Customer,AdminCustomer)
admin.site.register(Transfer,AdminTransfer)