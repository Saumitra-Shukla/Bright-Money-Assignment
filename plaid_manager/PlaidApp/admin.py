from django.contrib import admin

from PlaidApp.models import BankItemModel,AccountModel,TransactionModel,APILogModel


admin.site.register(BankItemModel)
admin.site.register(AccountModel)
admin.site.register(TransactionModel)

class APILogRegister(admin.ModelAdmin):
	readonly_fields = ('date_log',)
admin.site.register(APILogModel,APILogRegister)