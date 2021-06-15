from django.db import models

# Create your models here.
class Customer(models.Model):
    account_no=models.CharField(max_length=10)
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.CharField(max_length=10)
    balance=models.IntegerField()

class Transfer(models.Model):
    from_account=models.CharField(max_length=10)
    to_account=models.CharField(max_length=10)
    amount=models.IntegerField()
    updated_at=models.DateTimeField(auto_now=True)


