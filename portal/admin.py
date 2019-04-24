from .models import Transaction, Customer
from django.contrib import admin

admin.site.site_header = 'Eway Print Administration'
admin.site.site_title = 'Eway Print'


class TransactionAdmin(admin.ModelAdmin):
    list_filter = ['color_model', 'printed', 'upload_on']
    list_display = ['customer', 'otp_1', 'otp_2', 'payment_mode', 'amount', 'color_model', 'upload_on']


class CustomerAdmin(admin.ModelAdmin):
    pass


admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Customer, CustomerAdmin)

