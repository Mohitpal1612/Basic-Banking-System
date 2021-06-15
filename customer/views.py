from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import psycopg2 as pg

def customer_details(request):
    rows= Customer.objects.all()
    return render(request,'customer_detail.html', {'rows':rows})

def customer_bank_detail(request,id):
    row=Customer.objects.get(id=id)    
    return render(request,"customer_by_account_no.html",{'row':row})

def transaction(request):
    from_account=request.POST['from_account']
    print(from_account)
    balance=request.POST['balance']
    to_account=request.POST['to_account']
    amount=request.POST['amount']
    print(balance,amount)
    btn=request.POST['btn']
    if(btn=='Back'):
        return customer_details(request)
    else:
        b=balance
        q=Customer.objects.filter(account_no=from_account).update(balance=int(b)-int(amount))
        r=Customer.objects.filter(account_no=to_account).update(balance=30000)
        s=Transfer(from_account=from_account,to_account=to_account,amount=amount)
        s.save()
        return customer_details(request)
