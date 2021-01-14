from django.db import models

from CustomUser.models import CustomUserModel

class BankItemModel(models.Model):
	bank_item_id = models.CharField(max_length=300, unique=True)
	access_token = models.CharField(max_length=300, unique=True)
	request_id = models.CharField(max_length=200)
	user = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE)

class AccountModel(models.Model):
	account_id = models.CharField(max_length=100)
	bank_item = models.ForeignKey(BankItemModel, on_delete=models.CASCADE)
	balance_available = models.FloatField(default=None, null=True)
	balance_current = models.FloatField()


class TransactionModel(models.Model):
	transaction_id = models.CharField(max_length=100)
	account = models.ForeignKey(AccountModel, on_delete=models.CASCADE)
	amount = models.FloatField()
	date = models.DateField()
	name = models.CharField(max_length=100)
	pending = models.BooleanField()

class APILogModel(models.Model):
	request_id = models.CharField(max_length=200, unique=True)
	api_type = models.CharField(max_length=200)
	date_log = models.DateTimeField(verbose_name='date_log', auto_now_add=True)
